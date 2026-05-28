# RAG 知识库问答系统

基于 LangChain 的本地知识库问答系统，支持文档检索、上下文注入和带来源引用的智能回答。

## 功能特点

- **语义检索**：使用本地 Embedding 模型（Qwen3-Embedding-0.6B）将文档向量化，基于语义相似度检索相关片段。
- **带来源回答**：模型回答基于检索到的文档片段，每个回答展示命中片段和来源引用。
- **拒答能力**：当知识库中没有相关信息时，系统明确提示资料不足，不编造内容。
- **质量评估体系**：建立了分类测试问题集（知识库内 / 知识库边界 / 知识库外），可追踪回答质量变化。

## 技术栈

| 组件 | 技术 |
|------|------|
| RAG 框架 | LangChain |
| 向量数据库 | Chroma |
| Embedding 模型 | Qwen3-Embedding-0.6B（本地部署） |
| 大语言模型 | DeepSeek API |
| 前端展示 | Streamlit |
| Prompt 工程 | ChatPromptTemplate + 拒答约束 + 完整提取指令 |

## 项目结构

```text
stuLangchain/
├── data/
│   └── intro.txt              # 知识库文档
├── models/
│   └── Qwen3-Embedding-0.6B/  # 本地 Embedding 模型（不上传）
├── docs/
│   ├── Day2/
│   │   └── day2.py            # RAG 核心逻辑（检索、拼接、问答）
│   ├── Day3/
│   │   └── cli_rag_demo.py    # 命令行版 RAG Demo
│   ├── Day4/
│   │   └── streamlit_rag_demo.py  # Streamlit 网页版 RAG Demo
│   └── Day8/
│       └── rag_test_questions.md  # 分类测试问题集与测试记录
├── .env.example               # 环境变量模板
└── README.md
```

## 快速开始

### 1. 环境准备

```powershell
# 创建虚拟环境
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 安装依赖
pip install langchain langchain-deepseek langchain-chroma langchain-huggingface langchain-text-splitters streamlit python-dotenv
```

### 2. 配置

```powershell
# 复制环境变量模板并填写 API Key
copy .env.example .env
```

在 `.env` 中填写：

```text
DEEPSEEK_API_KEY=你的DeepSeek API Key
```

将本地 Embedding 模型放到 `models/Qwen3-Embedding-0.6B/` 目录。

### 3. 运行

**Streamlit 网页版**（推荐）：

```powershell
.\.venv\Scripts\python.exe -m streamlit run docs\Day4\streamlit_rag_demo.py
```

**命令行版**：

```powershell
.\.venv\Scripts\python.exe docs\Day3\cli_rag_demo.py
```

### 4. 示例问题

```text
RAG 的关键步骤是什么？
Prompt 模板在 RAG 中有什么作用？
Document.metadata 可以用来做什么？
LangGraph 是什么？
```

## RAG 流程

```text
用户提问
  → 问题向量化（Embedding）
  → 在向量库中检索相似片段（top_k=4）
  → 将命中片段 + 问题填入 Prompt 模板
  → 大模型生成回答
  → 展示回答 + 命中片段 + 来源引用
```

## 质量优化

项目实践了两种 RAG 质量优化手段：

**1. 知识库补强**

发现某类问题无法回答时，向知识库补充相关内容，重新构建向量库后复测验证。

**2. Prompt 优化**

发现命中片段包含信息但回答遗漏时，在 Prompt 中增加"完整提取要点"指令，提升回答完整度。

两种优化均形成"发现问题 → 分析原因 → 最小修改 → 复测验证"的闭环。

## 当前参数

```text
chunk_size = 200      # 每个文本块的字符数
chunk_overlap = 30    # 相邻块的重叠字符数
top_k = 4             # 检索返回的片段数量
temperature = 0.2     # 模型生成温度
```

## 学习记录

| 阶段 | 内容 |
|------|------|
| Day1 | DeepSeek API 调用、最小 RAG 流程 |
| Day2 | LCEL 链式调用、Embedding、Chroma 向量库、参数对比实验 |
| Day3 | 命令行交互版 RAG Demo |
| Day4 | Streamlit 网页版 RAG Demo |
| Day5 | 空检索异常处理 |
| Day6 | Demo 页面展示优化 |
| Day7 | 固定问题集测试、知识库补强闭环 |
| Day8 | 分类测试问题集、Prompt 优化闭环 |
