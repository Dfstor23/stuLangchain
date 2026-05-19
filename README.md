# stuLangchain

LangChain / RAG 学习记录项目。

当前主线：从最小 RAG Demo 开始，逐步掌握文档加载、文本切分、Embedding、Chroma 向量库、检索、Prompt 上下文注入和回答质量评估。

## 目录

- `data/intro.txt`：当前 RAG 示例知识库文本。
- `docs/Day1/`：Day1 学习代码与复习记录。
- `docs/Day2/`：Day2 LCEL、Embedding、Chroma 和完整 RAG 复习记录。
- `AGENTS.md`：本项目长期带教规则。

## 本地准备

1. 创建并激活 Python 虚拟环境。
2. 安装项目运行所需依赖。
3. 复制 `.env.example` 为 `.env`，并填写 `DEEPSEEK_API_KEY`。
4. 将本地 embedding 模型放到：

```text
models/Qwen3-Embedding-0.6B
```

本地模型、`.env`、虚拟环境和 Chroma 数据库不会上传到 GitHub。

## 当前进度

- Day1：最小 RAG 流程和 DeepSeek 调用复习。
- Day2：LCEL、RunnablePassthrough、Embedding 语义检索、Chroma 向量库、完整 RAG、参数对比和回答质量评估。

## Day2 阶段结论

当前小知识库下的阶段性参数：

```text
chunk_size = 200
chunk_overlap = 30
top_k = 4
```

已完成的评估：

- `top_k` 对比：`k` 变大能补充上下文，但可能引入无关片段。
- `chunk_size` 对比：过小会切碎信息，过大可能混入泛化内容。
- `chunk_overlap` 对比：可减少信息断裂，但当前短文档里效果不明显。
- 固定问题集评估：发现 `Prompt 模板` 和 `Document.metadata` 相关知识库内容不足。
- 知识库补强：补充 `Prompt 模板` 和 `Document.metadata` 后，检索效果明显改善。
- 最终回答评估：`top_k=4` 能让“RAG 的关键步骤”回答补上第 5 步。

下一步：进入 Day3，先做一个最小 Streamlit 或命令行交互版 RAG Demo，让项目从“脚本实验”变成“可展示应用”。
