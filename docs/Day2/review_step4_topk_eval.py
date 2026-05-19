"""
Day2 复习第4步补充：top_k 检索对比
运行：python docs/Day2/review_step4_topk_eval.py

本步目标：观察同一个问题在 k=1、k=3、k=5 时，命中片段数量和内容如何变化。
"""

from day2 import build_or_refresh_vectorstore, load_and_split_docs, retrieve_context


QUESTION = "为什么需要 RAG ?"


def print_hits(vectorstore, k: int) -> None:
    hit_docs = retrieve_context(QUESTION, vectorstore, k=k)

    print("=" * 60)
    print(f"问题: {QUESTION}")
    print(f"top_k: {k}")
    print(f"实际返回片段数: {len(hit_docs)}")
    print("命中片段:")

    for doc in hit_docs:
        chunk_id = doc.metadata.get("chunk_id")
        print("-" * 40)
        print(f"chunk_id={chunk_id}")
        print(doc.page_content)


def main() -> None:
    docs = load_and_split_docs(chunk_size=150, chunk_overlap=30)
    vectorstore = build_or_refresh_vectorstore(docs)

    for k in [1, 3, 5]:
        print_hits(vectorstore, k)


if __name__ == "__main__":
    main()
