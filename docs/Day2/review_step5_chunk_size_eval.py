"""
Day2 复习第5步：chunk_size 切块大小对比
运行：python docs/Day2/review_step5_chunk_size_eval.py

本步目标：观察同一份文档在不同 chunk_size 下，会被切成多少块，以及检索命中的片段是否更完整。
"""

import shutil
from pathlib import Path

from langchain_chroma import Chroma

from day2 import build_embeddings, load_and_split_docs, retrieve_context


QUESTION = "RAG 的关键步骤是什么？"
CHROMA_BASE_DIR = Path(__file__).parent / "chroma_db_chunk_size_eval"


def build_vectorstore_for_chunk_size(chunk_size: int):
    docs = load_and_split_docs(chunk_size=chunk_size, chunk_overlap=30)
    embeddings = build_embeddings()

    persist_dir = CHROMA_BASE_DIR / f"chunk_{chunk_size}"
    if persist_dir.exists():
        shutil.rmtree(persist_dir)

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=str(persist_dir),
        collection_name=f"chunk_size_{chunk_size}",
    )
    return docs, vectorstore


def print_eval(chunk_size: int) -> None:
    docs, vectorstore = build_vectorstore_for_chunk_size(chunk_size)
    hit_docs = retrieve_context(QUESTION, vectorstore, k=3)

    print("=" * 60)
    print(f"chunk_size: {chunk_size}")
    print(f"切分后的文档块数量: {len(docs)}")
    print(f"问题: {QUESTION}")
    print("命中片段:")

    for doc in hit_docs:
        chunk_id = doc.metadata.get("chunk_id")
        print("-" * 40)
        print(f"chunk_id={chunk_id}")
        print(doc.page_content)


def main() -> None:
    for chunk_size in [100, 200, 400]:
        print_eval(chunk_size)


if __name__ == "__main__":
    main()
