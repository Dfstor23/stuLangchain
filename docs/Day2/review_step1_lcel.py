"""
Day2 复习第1步：搞懂 RunnablePassthrough 和 LCEL {}
运行：在项目根目录执行 ./.venv/Scripts/python.exe docs/Day2/review_step1_lcel.py
"""
import time
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel


# ========== 实验1：RunnablePassthrough 透传了什么？ ==========
def experiment1():
    print("=" * 40)
    print("实验1：RunnablePassthrough 透传了什么？")
    print("=" * 40)

    chain = RunnablePassthrough()

    result = chain.invoke("你好")
    print(f"输入: '你好'")
    print(f"输出: {result}")
    print()
    print(">>> 结论：输入什么，输出就是什么，原样透传。")


# ========== 实验2：{} 里两个 Runnable 是并行还是串行？ ==========
def experiment2():
    print("\n" + "=" * 40)
    print("实验2：{} 里两个 Runnable 是并行还是串行？")
    print("=" * 40)

    def task_a(x):
        time.sleep(2)
        print("  [task_a] 完成")
        return f"A处理了{x}"

    def task_b(x):
        time.sleep(2)
        print("  [task_b] 完成")
        return f"B处理了{x}"

    runnable_a = RunnableLambda(task_a)
    runnable_b = RunnableLambda(task_b)
    chain = RunnableParallel({"A结果": runnable_a, "B结果": runnable_b})

    start = time.time()
    result = chain.invoke(5)
    elapsed = time.time() - start

    print(f"输入: 5")
    print(f"输出: {result}")
    print(f"耗时: {elapsed:.1f} 秒")

    if elapsed < 3:
        print(">>> 并行！两个 task 同时执行。")
    else:
        print(">>> 串行！两个 task 一个接一个执行。")


# ========== 实验3：模拟 Day1 RAG 链的数据流 ==========
def experiment3():
    print("\n" + "=" * 40)
    print("实验3：模拟 Day1 RAG 链中 RunnablePassthrough 的角色")
    print("=" * 40)

    def fake_retrieve(question: str) -> str:
        print(f"  [检索器] 收到: {question}")
        return "资料内容：LangChain 支持模型调用、Prompt模板、RAG链路。"

    retriever = RunnableLambda(fake_retrieve)

    chain = RunnableParallel({
        "context": retriever,
        "question": RunnablePassthrough(),
    })

    result = chain.invoke("LangChain 有哪些能力？")
    print(f"\n拼好的字典:")
    print(f"  context : {result['context']}")
    print(f"  question: {result['question']}")
    print()
    print(">>> 用户输入同时给了 retriever（检索）和 question（保留原话）。")
    print(">>> 这就是 Day1 step3_rag_demo 里 RunnablePassthrough 的作用。")


# ========== 实验4：删掉 RunnablePassthrough 会怎样？ ==========
def experiment4():
    print("\n" + "=" * 40)
    print("实验4：如果 {} 里只有 context，没有 question 会怎样？")
    print("=" * 40)

    def fake_retrieve(question: str) -> str:
        return "某段资料..."

    retriever = RunnableLambda(fake_retrieve)

    chain = RunnableParallel({"context": retriever})

    result = chain.invoke("测试问题")
    print(f"字典的键: {list(result.keys())}")
    print(">>> 发现了吗？字典里只有 'context'，没有 'question'。")
    print(">>> 后面 prompt 如果需要 {question}，就会因缺值而报错。")


if __name__ == "__main__":
    experiment1()
    experiment2()
    experiment3()
    experiment4()
