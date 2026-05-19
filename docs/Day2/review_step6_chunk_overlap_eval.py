"""
Day2 复习第6步：chunk_overlap 重叠长度对比
运行：python docs/Day2/review_step6_chunk_overlap_eval.py

本步目标：观察同一份文档在不同 chunk_overlap 下，命中片段是否能减少信息断裂。
"""

import shutil
from pathlib import Path

from langchain_chroma import Chroma

from day2 import build_embeddings, load_and_split_docs, retrieve_context


QUESTION = "Prompt 模板有什么作用？"
CHUNK_SIZE = 200
CHROMA_BASE_DIR = Path(__file__).parent / "chroma_db_chunk_overlap_eval"


def build_vectorstore_for_overlap(chunk_overlap: int):
    docs = load_and_split_docs(chunk_size=CHUNK_SIZE, chunk_overlap=chunk_overlap)
    embeddings = build_embeddings()

    persist_dir = CHROMA_BASE_DIR / f"overlap_{chunk_overlap}"
    if persist_dir.exists():
        shutil.rmtree(persist_dir)

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=str(persist_dir),
        collection_name=f"chunk_overlap_{chunk_overlap}",
    )
    return docs, vectorstore


def print_eval(chunk_overlap: int) -> None:
    docs, vectorstore = build_vectorstore_for_overlap(chunk_overlap)
    hit_docs = retrieve_context(QUESTION, vectorstore, k=3)

    print("=" * 60)
    print(f"chunk_size: {CHUNK_SIZE}")
    print(f"chunk_overlap: {chunk_overlap}")
    print(f"切分后的文档块数量: {len(docs)}")
    print(f"问题: {QUESTION}")
    print("命中片段:")

    for doc in hit_docs:
        chunk_id = doc.metadata.get("chunk_id")
        print("-" * 40)
        print(f"chunk_id={chunk_id}")
        print(doc.page_content)


def main() -> None:
    for chunk_overlap in [0, 30, 80]:
        print_eval(chunk_overlap)


if __name__ == "__main__":
    main()
