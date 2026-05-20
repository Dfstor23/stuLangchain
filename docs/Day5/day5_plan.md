# Day5 任务规划 - Streamlit RAG 异常处理优化

## Day5 总目标

继续打磨 Day4 的 Streamlit 网页 RAG Demo，让页面在检索结果不足时给出清楚提示。

目标不是增加新功能，而是先让 Demo 更稳定：

```text
用户输入问题
-> 系统检索知识库
-> 如果没有命中片段，页面提示资料不足
-> 如果有命中片段，正常展示回答、命中片段和来源引用
```

## Day4 已有基础

可以复用：

- `docs/Day4/streamlit_rag_demo.py`
- `docs/Day2/day2.py` 中的核心函数：
  - `build_llm()`
  - `load_and_split_docs()`
  - `build_or_refresh_vectorstore()`
  - `ask_with_trace()`

当前页面已支持：

- 输入问题。
- 点击按钮提交。
- 展示模型回答。
- 展示命中片段。
- 展示来源引用。

## Day5 学习路径

### 第 1 步：处理空检索结果

目标：

当 `result["hits"]` 为空时，页面提示：

```text
资料中没有足够信息。
```

为什么要做：

- 检索不到资料时继续展示回答，容易让模型产生幻觉。
- RAG Demo 要体现“资料不足就明确拒答”的能力。
- 这是从“能跑”走向“更可靠”的最小一步。

最小改造位置：

```text
docs/Day4/streamlit_rag_demo.py
```

计划逻辑：

```text
result = ask_with_trace(...)
if not result["hits"]:
    st.warning("资料中没有足够信息。")
    st.stop()
```

运行命令：

```powershell
.\.venv\Scripts\python.exe -m streamlit run docs\Day4\streamlit_rag_demo.py
```

预期输出：

- 如果命中片段为空，页面只显示资料不足提示。
- 如果命中片段不为空，页面正常显示模型回答、命中片段和来源引用。

常见报错：

- `KeyError: 'hits'`：检查 `ask_with_trace()` 是否返回了 `hits`。
- `NameError: name 'st' is not defined`：检查是否导入了 `streamlit as st`。
- 页面没有停止继续往下展示：检查是否写了 `st.stop()`。

必须掌握的知识点：

- `if not result["hits"]` 可以判断检索结果为空。
- `st.warning()` 用于在页面显示提示信息。
- `st.stop()` 用于停止 Streamlit 后续代码执行。
- 空检索处理可以降低模型幻觉风险。

### 第 2 步：补充 README 的异常提示说明

目标：

让 README 说明页面遇到资料不足时会提示，而不是强行回答。

暂时不做：

- 改 Prompt。
- 新增测试问题集。
- 上传文档。

### 第 3 步：记录 Day5 复盘

目标：

把当天完成内容、检查题、报错和下一步写入 Day5 复盘文件。

## 下一次只推进的最小任务

只做第 1 步：

```text
处理 Streamlit 页面空检索结果
```

完成后再出 5 个检查题，确认能解释这个异常处理逻辑后，再进入后续步骤。
