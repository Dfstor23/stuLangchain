"""
Day9 第 3 步：Function Calling 完整闭环

工具调用后把结果送回模型，让模型生成最终自然语言回答。

运行命令：
    .\.venv\Scripts\python.exe docs\Day9\agent_demo.py
"""

from __future__ import annotations

import os
from datetime import datetime

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek

load_dotenv()


# ── 第 1 部分：定义工具 ──

@tool
def get_current_time() -> str:
    """获取当前日期和时间。当用户询问现在几点、今天日期、当前时间时调用此工具。"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


TOOLS = [get_current_time]
TOOL_MAP = {t.name: t for t in TOOLS}


# ── 第 2 部分：创建模型并绑定工具 ──

def build_llm_with_tools():
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("缺少 DEEPSEEK_API_KEY")

    llm = ChatDeepSeek(
        model="deepseek-v4-flash",
        temperature=0.2,
        api_key=api_key,
    )
    return llm.bind_tools(TOOLS)


# ── 第 3 部分：完整工具调用闭环 ──

def ask(question: str, llm_with_tools) -> str:
    messages = [HumanMessage(content=question)]

    response = llm_with_tools.invoke(messages)

    if not response.tool_calls:
        return response.content

    print(f"  [调试] 模型要求调用工具：")
    messages.append(response)

    for tc in response.tool_calls:
        print(f"    工具：{tc['name']}，参数：{tc['args']}")
        result = TOOL_MAP[tc["name"]].invoke(tc["args"])
        print(f"    返回：{result}")
        messages.append(
            ToolMessage(content=str(result), tool_call_id=tc["id"])
        )

    final_response = llm_with_tools.invoke(messages)
    return final_response.content


# ── 第 4 部分：测试 ──

def main():
    llm_with_tools = build_llm_with_tools()

    test_questions = [
        "现在几点了？",
        "你好，请做一下自我介绍。",
        "今天是几月几号？",
    ]

    for question in test_questions:
        print(f"\n{'=' * 50}")
        print(f"问题：{question}")
        answer = ask(question, llm_with_tools)
        print(f"最终回答：{answer}")


if __name__ == "__main__":
    main()
