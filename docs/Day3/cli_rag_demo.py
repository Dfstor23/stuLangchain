r"""
Day3 第 1 步：命令行交互版 RAG Demo

运行命令：
    .\.venv\Scripts\python.exe docs\Day3\cli_rag_demo.py

功能：
1. 启动后构建 Chroma 向量库。
2. 接收用户输入的问题。
3. 检索 top_k=4 个命中文档片段。
4. 打印命中片段和模型回答。
5. 输入 exit 退出。
"""

from __future__ import annotations

import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

CURRENT_DIR = Path(__file__).resolve().parent
DAY2_DIR = CURRENT_DIR.parent / "Day2"
sys.path.append(str(DAY2_DIR))

from day2 import (  # noqa: E402  # pyright: ignore[reportMissingImports]
    ask_with_trace,
    build_llm,
    build_or_refresh_vectorstore,
    load_and_split_docs,
)


CHUNK_SIZE = 200
CHUNK_OVERLAP = 30
TOP_K = 4


def print_hits(hit_docs) -> None:
    print("\n命中片段：")
    for index, doc in enumerate(hit_docs, start=1):
        source = doc.metadata.get("source")
        chunk_id = doc.metadata.get("chunk_id")

        print("-" * 60)
        print(f"片段 {index} | source={source} | chunk_id={chunk_id}")
        print(doc.page_content)


def print_sources(hit_docs) -> None:
    print("\n候选来源：")
    for doc in hit_docs:    
        source = Path(doc.metadata.get("source")).name
        chunk_id = doc.metadata.get("chunk_id")
        print(f"- source={source}, chunk_id={chunk_id}")


def main() -> None:
    try:
        llm = build_llm()
    except ValueError as error:
        print(f"启动失败：{error}")
        print("请先在项目根目录的 .env 文件中配置 DEEPSEEK_API_KEY。")
        return

    print("正在构建 RAG 知识库，请稍等...")
    docs = load_and_split_docs(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    vectorstore = build_or_refresh_vectorstore(docs)

    print("RAG Demo 已启动。输入问题开始问答，输入 exit 或 quit 退出。")
    print(f"当前参数：chunk_size={CHUNK_SIZE}, chunk_overlap={CHUNK_OVERLAP}, top_k={TOP_K}")

    while True:
        question = input("\n请输入问题：").strip()
        if question.lower() in ["exit", "quit", "q"]:
            print("已退出。")
            break
        if not question:
            print("问题不能为空，请重新输入。")
            continue

        result = ask_with_trace(question, vectorstore, llm, k=TOP_K)
        if not result["hits"]:
            print("\n资料中没有足够信息。")
            continue

        print_hits(result["hits"])

        print("\n模型回答：")
        print(result["answer"])
        print_sources(result["hits"])


if __name__ == "__main__":
    main()
