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
- Day2：LCEL、RunnablePassthrough、Embedding 语义检索、Chroma 向量库、完整 RAG 和 `k` 参数对比。

下一步：用固定问题集对比 `chunk_size`、`chunk_overlap`、`top_k` 对检索结果和回答质量的影响。
