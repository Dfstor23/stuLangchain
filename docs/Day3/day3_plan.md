# Day3 任务规划

## Day3 总目标

把 Day2 的 RAG 脚本实验，推进成一个最小可交互 RAG Demo。

目标不是一次做完整项目，而是先做到：

```text
用户输入问题
→ 系统检索知识库
→ 打印命中片段
→ 调用 LLM 生成回答
→ 人工判断回答质量
```

---

## 当前基础

Day2 已完成：

- 文档加载与切分：`chunk_size`、`chunk_overlap`
- Embedding 向量化
- Chroma 向量库检索
- `top_k` 参数对比
- 固定问题集检索评估
- 知识库内容补强
- 最终回答质量评估

当前阶段性参数：

```text
chunk_size = 200
chunk_overlap = 30
top_k = 4
```

---

## Day3 学习路径

### 第 1 步：命令行交互版 RAG Demo

目标：

让用户可以在终端反复输入问题，程序返回命中片段和模型回答。

为什么先做命令行：

- 比 Streamlit 更简单。
- 更容易看清 RAG 主流程。
- 方便先验证功能，再做展示界面。

产出文件：

```text
docs/Day3/cli_rag_demo.py
```

预期运行方式：

```powershell
.\.venv\Scripts\python.exe docs\Day3\cli_rag_demo.py
```

预期效果：

```text
请输入问题：RAG 的关键步骤是什么？

命中片段：
- chunk_id=...

模型回答：
...
```

---

### 第 2 步：增加退出命令和异常提示

目标：

让命令行 Demo 更像一个可用工具。

计划支持：

- 输入 `exit` 退出程序。
- 没有配置 `DEEPSEEK_API_KEY` 时给出清晰提示。
- 检索不到内容时提示“资料中没有足够信息”。

---

### 第 3 步：增加来源引用输出

目标：

让回答后面能看到答案来自哪些片段。

计划输出：

```text
来源：
- source=data/intro.txt, chunk_id=3
- source=data/intro.txt, chunk_id=4
```

为什么重要：

- RAG 项目要体现“回答有据可查”。
- 面试或简历中可以强调“支持来源追踪”。

---

### 第 4 步：整理 README 的使用说明

目标：

让别人打开 GitHub 仓库后，能知道怎么运行 Demo。

计划补充：

- 环境变量说明
- 本地模型路径说明
- 命令行 Demo 运行命令
- 示例问题

---

## 暂时不做的内容

以下内容先不进入 Day3 第 1 阶段：

- Streamlit 页面
- 多文件上传
- PDF 解析
- Agent 工具调用
- LangGraph
- Docker 部署

原因：

当前优先目标是先把一个最小 RAG 应用讲清楚、跑稳定、能展示。

---

## 下一次开始任务

下一次只做第 1 步：

```text
docs/Day3/cli_rag_demo.py
```

最小功能：

1. 启动后构建 Chroma 向量库。
2. 加载 DeepSeek LLM。
3. 接收用户输入的问题。
4. 检索 `top_k=4` 个片段。
5. 打印命中片段和模型回答。
6. 输入 `exit` 退出。

完成后再出 5 个检查题，确认能解释主流程后再进入下一步。
