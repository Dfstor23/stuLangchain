"""
LangChain + DeepSeek 入门（Day1）

运行前准备：
1) 在 DeepSeek 开放平台创建 API Key
2) 设置环境变量（PowerShell）:
   $env:DEEPSEEK_API_KEY="你的key"
3) 使用项目虚拟环境运行:
   ./.venv/Scripts/python.exe day1.py
"""

from __future__ import annotations 


import os
from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_deepseek import ChatDeepSeek
from langchain_text_splitters import RecursiveCharacterTextSplitter


BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "intro.txt"


def build_model() -> ChatDeepSeek:
    """创建 DeepSeek 聊天模型实例。"""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError(
            "未检测到 DEEPSEEK_API_KEY，请先在终端设置环境变量后重试。"
        )
    return ChatDeepSeek(model="deepseek-chat", temperature=0.2, api_key=api_key)


def step1_basic_chat(model: ChatDeepSeek) -> None:
    """步骤1：最简单的模型调用。"""
    print("\n=== 步骤 1：基础调用 ===")
    question = "用3句话介绍一下什么是LangChain。"
    result = model.invoke(question)
    print(f"问题: {question}\n")
    print("模型回答:")
    print(result.content)


def step2_prompt_template(model: ChatDeepSeek) -> None:
    """步骤2：使用 Prompt 模板进行结构化提问。"""
    print("\n=== 步骤 2：Prompt 模板 ===")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个耐心的 AI 导师，回答要简洁、准确。"),
            ("human", "我是{level}，请用{style}解释：{topic}"),
        ]
    )
    chain = prompt | model | StrOutputParser()
    answer = chain.invoke(
        {
            "level": "LangChain 初学者",
            "style": "生活化类比",
            "topic": "PromptTemplate 的作用",
        }
    )
    print(answer)


def load_docs() -> List[Document]:
    """加载并切分本地知识库文档。"""
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"找不到文件: {DATA_FILE}")

    text = DATA_FILE.read_text(encoding="utf-8")
    splitter = RecursiveCharacterTextSplitter(chunk_size=120, chunk_overlap=20)
    chunks = splitter.split_text(text)
    return [Document(page_content=chunk) for chunk in chunks]


def simple_retrieve(question: str, docs: List[Document], top_k: int = 3) -> str:
    """一个轻量级关键词检索器（方便 Day1 理解 RAG 流程）。"""
    keywords = [word.strip("，。！？,.!? ").lower() for word in question.split()]
    scored = []
    for doc in docs:
        content = doc.page_content.lower()
        score = sum(1 for kw in keywords if kw and kw in content)
        scored.append((score, doc.page_content))
    scored.sort(key=lambda x: x[0], reverse=True)
    selected = [item[1] for item in scored[:top_k]]
    return "\n".join(f"- {item}" for item in selected)


def step3_rag_demo(model: ChatDeepSeek) -> None:
    """步骤3：本地文件问答（轻量 RAG）。"""
    print("\n=== 步骤 3：本地 RAG Demo ===")
    docs = load_docs()

    retriever = RunnableLambda(lambda q: simple_retrieve(q, docs))
    prompt = ChatPromptTemplate.from_template(
        "你是知识库问答助手，只能根据给定资料回答。\n\n"
        "资料:\n{context}\n\n"
        "问题: {question}\n"
        "如果资料不足，请明确说“资料中没有足够信息”。"
    )

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    question = "LangChain 的核心能力有哪些？"
    answer = rag_chain.invoke(question)
    context_preview = simple_retrieve(question, docs)

    print("检索到的资料片段:")
    print(context_preview)
    print("\n回答:")
    print(answer)


def print_learning_path() -> None:
    print("\n========== 学习路径（建议按顺序） ==========")
    print("1. 看 step1：理解“LangChain 调模型”的最小闭环。")
    print("2. 看 step2：学会 Prompt 模板化，参数化你的输入。")
    print("3. 看 step3：理解 RAG = 检索 + 生成。")
    print("4. 练习：把 data/intro.txt 改成你自己的笔记，重复问答。")
    print("5. 进阶：下一步可以加向量库（FAISS / Chroma）和 Embeddings。")
    print("==========================================\n")


def main() -> None:
    print_learning_path()
    model = build_model()
    step1_basic_chat(model)
    step2_prompt_template(model)
    step3_rag_demo(model)


if __name__ == "__main__":
    main()
