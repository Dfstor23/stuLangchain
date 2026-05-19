"""
Day2 复习第8步：RAG 最终回答质量评估
运行：python docs/Day2/review_step8_answer_eval.py

本步目标：在检索结果改善后，调用 LLM 生成回答，并观察回答是否基于命中片段。
"""

import shutil
from pathlib import Path

from langchain_chroma import Chroma

from day2 import (
    ask_with_trace,
    build_embeddings,
    build_llm,
    load_and_split_docs,
)


CHUNK_SIZE = 200
CHUNK_OVERLAP = 30
TOP_K = 4
CHROMA_DIR = Path(__file__).parent / "chroma_db_answer_eval"

QUESTIONS = [
    "RAG 的关键步骤是什么？",
]


def build_vectorstore():
    docs = load_and_split_docs(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    embeddings = build_embeddings()

    if CHROMA_DIR.exists():
        shutil.rmtree(CHROMA_DIR)

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
        collection_name="answer_eval",
    )
    return vectorstore


def main() -> None:
    vectorstore = build_vectorstore()
    llm = build_llm()

    print("固定参数:")
    print(f"- chunk_size={CHUNK_SIZE}")
    print(f"- chunk_overlap={CHUNK_OVERLAP}")
    print(f"- top_k={TOP_K}")

    for index, question in enumerate(QUESTIONS, start=1):
        result = ask_with_trace(question, vectorstore, llm, k=TOP_K)

        print("\n" + "=" * 70)
        print(f"问题{index}: {question}")
        print("命中片段:")

        for doc in result["hits"]:
            chunk_id = doc.metadata.get("chunk_id")
            print("-" * 40)
            print(f"chunk_id={chunk_id}")
            print(doc.page_content)

        print("\n模型回答:")
        print(result["answer"])
        print("\n人工判断: [待填写：好 / 一般 / 差]")
        print("原因: [待填写：是否基于资料、是否完整、是否编造]")


if __name__ == "__main__":
    main()
