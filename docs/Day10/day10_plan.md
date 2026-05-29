# Day10 任务规划 - RAG + Agent 结合：让模型自己决定查知识库

## Day10 总目标

把 Day1-Day8 的 RAG 检索做成 Agent 的一个工具，和 Day9 的时间工具并列，让模型自己决定：该查知识库还是该调其他工具。

```text
用户提问
→ 模型判断：这个问题需要查知识库？还是查时间？还是直接回答？
→ 调用对应工具
→ 把工具结果送回模型
→ 模型生成最终回答
```

## Day9 已有基础

可以复用：

- `docs/Day9/agent_demo.py`：Function Calling 完整闭环。
- `docs/Day2/day2.py`：RAG 核心逻辑（检索、拼接、问答）。
- `data/intro.txt`：知识库文档。

Day9 已完成：

- 定义工具、绑定工具、工具调用闭环。
- 模型能自主区分"需要调工具"和"直接回答"。

## Day10 学习路径

### 第 1 步：把 RAG 检索包装成一个工具

目标：

用 `@tool` 装饰器把现有的 RAG 检索逻辑封装成 `search_knowledge_base(query: str)` 工具。

为什么要做：

- RAG 变成 Agent 的一个工具后，模型可以自主决定什么时候查知识库。
- 不需要查知识库的问题（如"现在几点"）就不会走检索流程。
- 这是 RAG 和 Agent 结合的最基础形态。

### 第 2 步：多工具 Agent 测试

目标：

同时绑定 `search_knowledge_base` 和 `get_current_time` 两个工具，用不同类型的问题测试模型选择：

- 知识库问题："RAG 的关键步骤是什么？" → 预期调用 search_knowledge_base
- 时间问题："现在几点了？" → 预期调用 get_current_time
- 闲聊问题："你好" → 预期直接回答

### 第 3 步：观察并记录多工具选择行为

目标：

记录模型在多工具场景下的选择行为，观察是否有误判。

暂时不做：

- LangGraph 状态图。
- 多轮对话记忆。
- ReAct 推理链。
- Streamlit 页面。

## 下一次只推进的最小任务

先完成第 1 步：把 RAG 检索包装成 `search_knowledge_base` 工具。
