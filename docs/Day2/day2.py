from __future__ import annotations

import os
from pathlib import Path
from typing import List, Dict, Any

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_deepseek import ChatDeepSeek
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Chroma + Embeddings
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


load_dotenv()

# day2.py 位于 docs/Day2/，parents[2] 才是项目根 stuLangchain/
ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = ROOT_DIR / "data" / "intro.txt"
MODEL_PATH = ROOT_DIR / "models" / "Qwen3-Embedding-0.6B"
CHROMA_DIR = Path(__file__).parent / "chroma_db"


def build_llm() -> ChatDeepSeek:
    """DeepSeek 聊天模型"""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("缺少 DEEPSEEK_API_KEY")
    return ChatDeepSeek(model="deepseek-v4-flash", temperature=0.2, api_key=api_key)


def load_and_split_docs(chunk_size: int = 150, chunk_overlap: int = 30) -> List[Document]:
    """读取并切分文档"""
    text = DATA_FILE.read_text(encoding="utf-8")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    chunks = splitter.split_text(text)

    # 给每个 chunk 增加 metadata，后面可用于来源追踪
    docs: List[Document] = []
    for i, c in enumerate(chunks):
        docs.append(
            Document(
                page_content=c,
                metadata={"source": str(DATA_FILE), "chunk_id": i},
            )
        )
    return docs


def build_embeddings() -> HuggingFaceEmbeddings:
    """本地中文 embedding（不依赖 OpenAI）"""
    return HuggingFaceEmbeddings(
        model_name=str(MODEL_PATH),
        model_kwargs={"device": "cpu", "trust_remote_code": True},  # 有 GPU 可改成 cuda
        encode_kwargs={"normalize_embeddings": True},
    )


def build_or_refresh_vectorstore(docs: List[Document]) -> Chroma:
    """
    构建并持久化向量库
    Day2 建议先每次重建，方便你观察参数影响
    """
    embeddings = build_embeddings()

    # 重建（教学阶段更直观）
    if CHROMA_DIR.exists():  
        import shutil
        shutil.rmtree(CHROMA_DIR)

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
        collection_name="day2_intro",
    )
    return vectorstore


def retrieve_context(question: str, vectorstore: Chroma, k: int = 3) -> List[Document]:
    """语义检索"""
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    return retriever.invoke(question)


def format_context(docs: List[Document]) -> str:
    """把检索到的文档拼接成上下文字符串"""
    return "\n\n".join(
        [f"[片段{i+1}] {d.page_content}" for i, d in enumerate(docs)]
    )


def build_rag_chain(llm: ChatDeepSeek):
    """RAG 问答链"""
    prompt = ChatPromptTemplate.from_template(
        "你是知识库问答助手，只能根据给定资料回答。\n"
        "请尽量完整地列出资料中提到的所有相关要点，不要遗漏。\n\n"
        "资料如下：\n{context}\n\n"
        "问题：{question}\n"
        "若资料不足，请明确回答：资料中没有足够信息。"
    )
    chain = prompt | llm | StrOutputParser()
    return chain


#完整RAG核心流程  （把问题和检索到的文档一同送给模型）
def ask_with_trace(question: str, vectorstore: Chroma, llm: ChatDeepSeek, k: int = 3) -> Dict[str, Any]:
    """问答 + 打印检索轨迹（Day2重点）"""
    hit_docs = retrieve_context(question, vectorstore, k=k) 
    context = format_context(hit_docs)

    rag_chain = build_rag_chain(llm)
    answer = rag_chain.invoke({"context": context, "question": question})

    return {
        "question": question,
        "hits": hit_docs,
        "answer": answer,
    }


def run_eval_questions(vectorstore: Chroma, llm: ChatDeepSeek) -> None:
    """固定问题集，做 Day2 对比实验"""
    questions = [
        "LangChain 的核心能力有哪些？",
        "RAG 的关键步骤是什么？",
        "Prompt 模板有什么作用？",
        "为什么要对文本切块？",
        "Document.metadata 可以用来做什么？",
    ]

    for q in questions:
        result = ask_with_trace(q, vectorstore, llm, k=1)
        print("\n" + "=" * 60)
        print(f"问题: {result['question']}")
        print("\n命中片段:")
        for d in result["hits"]:
            print(f"- chunk_id={d.metadata.get('chunk_id')} | {d.page_content}")
        print("\n回答:")
        print(result["answer"])


def main():
    llm = build_llm()
    docs = load_and_split_docs(chunk_size=150, chunk_overlap=30)
    vectorstore = build_or_refresh_vectorstore(docs)
    run_eval_questions(vectorstore, llm)


if __name__ == "__main__":
    main()