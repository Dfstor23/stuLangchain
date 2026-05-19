"""
Day2 复习第2步：从关键词检索 → 语义检索
运行：./.venv/Scripts/python.exe docs/Day2/review_step2_embedding.py

本步目标：亲眼看到关键词匹配失败，再用 embedding 向量相似度成功匹配。
"""
import os
from dotenv import load_dotenv

load_dotenv()


 # ========== 准备：模拟的两个句子 ==========
# 文档里的内容（你本地 intro.txt 的实际片段）
doc_sentence = "LangChain 是一个构建 LLM 应用的框架"

# 用户的问题（用了近义词/同义表达）
user_question = "大语言模型是什么？"


# ========== 实验1：关键词匹配 ==========
def experiment1_keyword():
    print("=" * 50)
    print("实验1：关键词匹配 —— Day1 的 simple_retrieve 方式")
    print("=" * 50)

    # Day1 的关键词打分逻辑
    keywords = [w.strip("，。！？,.!? ").lower() for w in user_question.split()]
    doc_lower = doc_sentence.lower()

    print(f"文档内容: {doc_sentence}")
    print(f"用户问题: {user_question}")
    print(f"拆出的关键词: {keywords}")

    score = sum(1 for kw in keywords if kw and kw in doc_lower)
    print(f"匹配得分: {score}")

    if score == 0:
        print()
        print(">>> 失败！虽然用户问的是 LLM 的同一个概念，")
        print(">>> 但\"大语言模型\"和\"LLM\"没有公共字，关键词匹配得 0 分。")
        print(">>> 这就是 Day1 检索器的根本缺陷。")
        experiment2_embedding()
    else:
        print(f">>> 匹配到 {score} 个关键词")


# ========== 实验2：Embedding 语义相似度 ==========
def experiment2_embedding():
    print("\n" + "=" * 50)
    print("实验2：Embedding 语义相似度 —— Day2 的升级方式")
    print("=" * 50)
    print("正在加载本地 embedding 模型（首次会下载，约 1 分钟）...")

    from langchain_huggingface import HuggingFaceEmbeddings
    import numpy as np

    MODEL_PATH = r"E:\cursorCode\stuLangchain\models\Qwen3-Embedding-0.6B"

    embeddings = HuggingFaceEmbeddings(
        model_name=MODEL_PATH,
        model_kwargs={"device": "cpu", "trust_remote_code": True},
        encode_kwargs={"normalize_embeddings": True},   # 归一化操作，才能计算余弦相似度
    )

    # 把两句话分别变成向量
    vec_doc = embeddings.embed_query(doc_sentence)
    vec_question = embeddings.embed_query(user_question)

    # 计算余弦相似度
    similarity = np.dot(vec_doc, vec_question)

    print(f"文档内容: {doc_sentence}")
    print(f"用户问题: {user_question}")
    print(f"向量维度: {len(vec_doc)}")
    print(f"余弦相似度: {similarity:.4f}")

    if similarity > 0.5:
        print()
        print(">>> 成功！两个句子字面完全不同，但向量相似度很高。")
        print(">>> Embedding 捕捉到了 \"LLM\" ≈ \"大语言模型\" 的语义关系。")
        print(">>> 这就是 Day2 用向量检索替代关键词检索的原因。")
    else:
        print("相似度较低，可能需要换一组更相近的句子测试。")


if __name__ == "__main__":
    experiment1_keyword()
    #experiment2_embedding()
