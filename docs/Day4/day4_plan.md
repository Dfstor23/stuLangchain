# Day4 任务规划 - 最小 Streamlit RAG 展示页面

## Day4 总目标

把 Day3 的命令行 RAG Demo 改造成一个最小可展示的网页 Demo。

目标不是一次做完整产品，而是先做到：

```text
用户在网页输入问题
-> 点击按钮
-> 页面展示模型回答
-> 页面展示命中片段
-> 页面展示来源引用
```

## Day3 已有基础

可以复用：

- `docs/Day3/cli_rag_demo.py` 的交互思路。
- `docs/Day2/day2.py` 里的核心函数：
  - `build_llm()`
  - `load_and_split_docs()`
  - `build_or_refresh_vectorstore()`
  - `ask_with_trace()`

当前阶段参数继续保持：

```text
chunk_size = 200
chunk_overlap = 30
top_k = 4
```

## 官方文档阅读判断

完成当前最小 Demo 前，必须确认：

1. Streamlit 如何启动一个 `.py` 页面。
2. Streamlit 如何接收文本输入。
3. Streamlit 如何展示普通文本和分块内容。

当前可以暂时跳过：

- Streamlit 多页面应用。
- 文件上传组件。
- 会话状态 `st.session_state` 的复杂用法。
- Streamlit 部署。
- LangChain 新 API 学习。

原因：

Day4 暂时不新增复杂 LangChain 能力，只把 Day3 已跑通的 RAG 主流程放到页面上。

## Day4 学习路径

### 第 1 步：复测 Day3 命令行 Demo

目标：

确认进入网页开发前，CLI 版本仍然能完整跑通。

为什么先做：

- Streamlit 只是展示层。
- 如果 CLI 本身不能回答，网页也无法正常回答。
- 先区分“RAG 核心问题”和“页面展示问题”。

运行命令：

```powershell
.\.venv\Scripts\python.exe docs\Day3\cli_rag_demo.py
```

测试问题：

```text
RAG 的关键步骤是什么？
Prompt 模板有什么作用？
Document.metadata 可以用来做什么？
```

预期输出：

```text
命中片段：
...

模型回答：
...

候选来源：
- source=intro.txt, chunk_id=...
```

常见报错：

- `缺少 DEEPSEEK_API_KEY`：检查项目根目录 `.env`。
- 找不到 embedding 模型：检查 `models/Qwen3-Embedding-0.6B`。
- 回答明显跑偏：先看命中片段是否相关。

必须掌握的知识点：

- Streamlit 页面只是调用已有 RAG 函数。
- 页面改造前必须先确认命令行基线稳定。
- 命中片段、模型回答、来源引用是 RAG Demo 的三个展示重点。

### 第 2 步：创建最小 Streamlit 页面

产出文件：

```text
docs/Day4/streamlit_rag_demo.py
```

最小功能：

- 页面标题。
- 问题输入框。
- 提交按钮。
- 调用已有 RAG 函数。
- 展示模型回答。

暂时不做：

- 美化页面。
- 上传文件。
- 多轮聊天记忆。

### 第 3 步：在页面展示命中片段

目标：

让用户能看到回答前模型检索到了哪些资料。

展示内容：

```text
片段序号
source
chunk_id
page_content
```

### 第 4 步：在页面展示来源引用

目标：

让网页 Demo 具备“答案可追溯”的项目亮点。

展示内容：

```text
- source=intro.txt, chunk_id=0
- source=intro.txt, chunk_id=1
```

### 第 5 步：补充 README 的 Day4 运行说明

目标：

让别人打开项目后，知道如何启动网页 Demo。

计划补充：

- Streamlit 运行命令。
- `.env` 检查说明。
- 示例问题。
- 当前功能边界。

## 下一次只推进的最小任务

只做第 1 步：

```text
复测 Day3 命令行 RAG Demo
```

通过标准：

1. 至少跑通 3 个示例问题。
2. 每个问题都能看到命中片段。
3. 每个问题都能看到模型回答。
4. 每个问题都能看到来源引用。
5. 能解释一次完整流程：输入问题 -> 检索 -> 注入上下文 -> 模型回答 -> 来源追踪。

通过后再进入第 2 步：创建最小 Streamlit 页面。
