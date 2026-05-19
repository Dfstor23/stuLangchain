"""
Day2 复习第7步：固定问题集评估检索结果
运行：python docs/Day2/review_step7_eval_questions.py

本步目标：用固定问题集观察检索命中的 chunk_id 和片段内容，为后续 RAG 质量评估表做准备。
"""

import shutil
from pathlib import Path

from langchain_chroma import Chroma

from day2 import build_embeddings, load_and_split_docs, retrieve_context


CHUNK_SIZE = 200
CHUNK_OVERLAP = 30
TOP_K = 3
CHROMA_DIR = Path(__file__).parent / "chroma_db_eval_questions"
#后面 Chroma.from_documents(..., persist_directory=str(CHROMA_DIR)) 
#会把 embedding 向量、文本块和 metadata 持久化到这个文件夹。下次运行如果不清空，Chroma 会接着用这里已有的数据。

QUESTIONS = [
    "LangChain 的核心能力有哪些？",
    "RAG 的关键步骤是什么？",
    "Prompt 模板有什么作用？",
    "为什么需要 RAG？",
    "Document.metadata 可以用来做什么？"
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
        collection_name="eval_questions",
    )
    return docs, vectorstore


def main() -> None:
    docs, vectorstore = build_vectorstore()

    print("固定参数:")
    print(f"- chunk_size={CHUNK_SIZE}")
    print(f"- chunk_overlap={CHUNK_OVERLAP}")
    print(f"- top_k={TOP_K}")
    print(f"- 文档块数量={len(docs)}")

    for index, question in enumerate(QUESTIONS, start=1):
        hit_docs = retrieve_context(question, vectorstore, k=TOP_K)
        hit_ids = [str(doc.metadata.get("chunk_id")) for doc in hit_docs]

        print("\n" + "=" * 70)
        print(f"问题{index}: {question}")
        print(f"命中 chunk_id: {', '.join(hit_ids)}")
        print("人工判断: [待填写：好 / 一般 / 差]")
        print("原因: [待填写：是否命中关键信息，是否混入无关片段]")
        print("命中片段:")

        for doc in hit_docs:
            chunk_id = doc.metadata.get("chunk_id")
            print("-" * 40)
            print(f"chunk_id={chunk_id}")
            print(doc.page_content)


if __name__ == "__main__":
    main()
