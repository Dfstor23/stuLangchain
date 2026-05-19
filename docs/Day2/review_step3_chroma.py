"""
Day2 复习第3步：Chroma 向量库完整链路
运行：./.venv/Scripts/python.exe docs/Day2/review_step3_chroma.py

本步目标：加载文档，切分成 Document，写入 Chroma，再检索命中片段。
"""
from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = ROOT_DIR / "data" / "intro.txt"
MODEL_PATH = ROOT_DIR / "models" / "Qwen3-Embedding-0.6B"
CHROMA_DIR = Path(__file__).parent / "chroma_db_step3"


def load_and_split_docs(chunk_size: int = 150, chunk_overlap: int = 30) -> list[Document]:
    """读取 intro.txt，并切成带 metadata 的 Document。"""
    text = DATA_FILE.read_text(encoding="utf-8")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    chunks = splitter.split_text(text)

    docs = []
    for i, chunk in enumerate(chunks):
        docs.append(
            Document(
                page_content=chunk,
                metadata={"source": str(DATA_FILE), "chunk_id": i},
            )
        )

    return docs


def build_embeddings() -> HuggingFaceEmbeddings:
    """加载本地 embedding 模型。"""
    return HuggingFaceEmbeddings(
        model_name=str(MODEL_PATH),
        model_kwargs={"device": "cpu", "trust_remote_code": True},
        encode_kwargs={"normalize_embeddings": True},
    )


def build_vectorstore(docs: list[Document]) -> Chroma:
    """把 Document 写入 Chroma 向量库。"""
    embeddings = build_embeddings()

    return Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),  
        collection_name="day2_step3",
    )


def print_hits(question: str, vectorstore: Chroma, k: int = 3) -> None:
    """检索并打印命中的 chunk。"""
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    results = retriever.invoke(question)

    print(f"\n问题: {question}")
    print("\n命中的片段:")
    for doc in results:
        print("-" * 40)
        print(f"chunk_id: {doc.metadata['chunk_id']}")
        print(doc.page_content)


def main() -> None:
    docs = load_and_split_docs()
    print(f"切分后的文档块数量: {len(docs)}")

    vectorstore = build_vectorstore(docs)
    print_hits("为什么需要 RAG?", vectorstore)


if __name__ == "__main__":
    main()
