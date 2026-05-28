r"""
Day4 第 2 步：最小 Streamlit RAG 展示页面

运行命令：
    .\.venv\Scripts\python.exe -m streamlit run docs\Day4\streamlit_rag_demo.py

当前功能：
1. 在网页输入问题。
2. 点击按钮提交问题。
3. 调用 Day2 已有 RAG 函数。
4. 展示模型回答、命中片段和来源引用。
"""

from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st
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


st.set_page_config(page_title="我的 RAG 知识库问答 Demo", page_icon="🔎")
st.title("我的 RAG 知识库问答 Demo")
st.write("输入一个问题，系统会从本地知识库检索相关片段，再结合大模型生成带来源参考的回答。")
st.caption(f"当前参数：chunk_size={CHUNK_SIZE}, chunk_overlap={CHUNK_OVERLAP}, top_k={TOP_K}")
st.markdown(
    """
**项目亮点：**

- 基于本地知识库检索相关片段。
- 回答结果展示命中片段和来源引用。
- 检索不到资料时明确提示，降低模型幻觉风险。
"""
)

question = st.text_input("请输入问题", placeholder="例如：RAG 的关键步骤是什么？")

if st.button("提交问题"):
    question = question.strip()

    if not question:
        st.warning("问题不能为空，请先输入问题。")
    else:
        try:
            with st.spinner("正在构建知识库并生成回答..."):
                llm = build_llm()
                docs = load_and_split_docs(
                    chunk_size=CHUNK_SIZE,
                    chunk_overlap=CHUNK_OVERLAP,
                )
                vectorstore = build_or_refresh_vectorstore(docs)
                result = ask_with_trace(question, vectorstore, llm, k=TOP_K)

                if not result["hits"]:
                    st.warning("抱歉，当前知识库未收录相关内容，建议查阅官方文档。")
                    st.stop()

            st.subheader("模型回答")
            st.write(result["answer"])

            st.subheader("命中片段")
            for index, doc in enumerate(result["hits"], start=1):
                source = Path(doc.metadata.get("source")).name
                chunk_id = doc.metadata.get("chunk_id")
                st.markdown(f"**片段 {index} | source={source} | chunk_id={chunk_id}**")
                st.write(doc.page_content)

            st.subheader("参考资料")
            for doc in result["hits"]:
                source = Path(doc.metadata.get("source")).name
                chunk_id = doc.metadata.get("chunk_id")
                st.write(f"- source={source}, chunk_id={chunk_id}")
        except ValueError as error:
            st.error(f"启动失败：{error}")
            st.info("请先在项目根目录的 .env 文件中配置 DEEPSEEK_API_KEY。")
