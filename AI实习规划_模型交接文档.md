# AI应用/AI产品实习规划模型交接文档

生成日期：2026-05-14  
用途：供其他AI模型或Agent快速理解用户背景、JD分析结论、学习路线与求职策略，继续提供一致的职业规划和学习陪跑建议。

## 1. 用户基本背景

用户是计算机相关专业本科在校生，目标是在2026年7-8月拿到AI应用开发或AI产品方向实习offer，并计划在2026年9月左右开始实习。

已知背景：

- 学校：广州城市理工学院，民办本科。
- 专业：计算机科学与技术。
- 年级：大三下。
- 绩点：约3.1/4.0。
- 英语：四级428分。
- 时间条件：一周课程较少，每天可投入6小时以上学习。
- 已学课程：C语言、C++、Python、数据结构、算法基础、数据库、计算机网络、操作系统、计算机组成原理、线性代数、概率论等。
- 项目经历：
  - C++面向对象课程设计，主要使用链表等数据结构。
  - Python书籍信息爬虫，属于简单爬虫项目。
  - Streamlit + DeepSeek API简易网页聊天助手，仅支持基础聊天。
- 竞赛：
  - 2025年广东省蓝桥杯C++ B组省级二等奖。
  - 参加过广东省ACM省赛，未获奖。
- 当前学习状态：
  - Python基础已重温。
  - 正在学习LangChain。
  - 已在Cursor中完成Day1学习：DeepSeek模型调用、Prompt模板、LCEL、轻量关键词RAG。
  - Day2开始接触Embedding、Chroma、向量RAG，但理解沉淀不足。

## 2. 资料来源和重要假设

分析基于用户提供的Boss直聘AI应用/AI产品方向实习岗位截图和整理文档。原始截图约34张，其中部分是同一岗位续页或重复岗位；结构化分析主要基于约26条可读JD。

样本岗位包括：

- AI应用开发实习生
- 大模型应用开发实习生
- Agent开发实习生
- AI应用研发实习生
- AI产品实习生
- AI智能体应用开发管培生
- AI工具应用类实习生
- 算法开发实习生（RAG与Agent）
- Vibe Coding实习生
- AI应用实习生/智能体开发

统一假设：

- 用户目标不是算法研究岗或大模型训练岗，而是AI应用层岗位。
- 用户短期最优路线是“AI应用开发主攻，AI产品/AI工作流/大模型评测/Prompt优化作为辅投或保底”。
- 用户学校背景不是优势，因此必须用可展示项目、GitHub、Demo视频、README、技术复盘来弥补。
- 用户不应将主要精力放在LoRA/SFT/RLHF/PyTorch模型训练上，除非后续转算法方向。

## 3. JD横向分析结论

### 3.1 高频硬技能

根据JD统计和归纳，AI应用开发/AI产品实习岗位高频要求如下：

| 能力 | 重要性 | 说明 |
|---|---|---|
| Python | 极高 | 几乎是AI应用开发岗基础门槛，用于脚本、API、RAG、数据处理 |
| LLM API调用 | 极高 | DeepSeek、Qwen、OpenAI、Claude、豆包等模型API调用 |
| Prompt Engineering | 极高 | 结构化输出、少样本、角色设定、稳定性优化、业务Prompt模板 |
| RAG/知识库 | 极高 | 文档切分、Embedding、向量库、检索、上下文注入、来源引用 |
| Agent/工作流 | 高 | 工具调用、Function Calling、流程编排、任务拆解 |
| LangChain/LlamaIndex | 中高 | 应用开发岗常见，尤其RAG/Agent岗位 |
| Dify/Coze/n8n | 中高 | 低代码AI工作流，适合快速POC和产品验证 |
| FastAPI/Flask/Streamlit | 中高 | Web化、接口化、Demo展示 |
| SQL/数据库/向量数据库 | 中高 | SQL、SQLite、MySQL、Chroma、FAISS、Milvus等 |
| Git/GitHub/Linux/Docker | 中 | 工程化交付、部署、协作 |
| MCP/Function Calling | 中 | 趋势项，岗位频率低于RAG/Agent，但作为加分项明显 |
| 文档解析 | 中 | PDF/Word转Markdown、非结构化数据处理，在知识库岗位常见 |
| 模型微调/部署 | 低中 | 算法/高阶岗位更看重，短期不是用户主线 |

### 3.2 高频软技能

JD反复强调：

- 自主学习能力。
- 逻辑拆解能力。
- 沟通协作能力。
- 信息搜集能力。
- 文档写作能力。
- 责任心和执行力。
- 能快速试错。
- 能主动发现业务AI化需求。
- 能把AI工具真正落地到业务流程。

### 3.3 AI应用开发岗 vs AI产品岗

| 维度 | AI应用开发岗 | AI产品岗 |
|---|---|---|
| 核心目标 | 把AI能力做成可运行系统 | 把业务问题定义成AI产品方案 |
| 核心能力 | Python、API、RAG、Agent、后端、部署、评测 | 需求分析、PRD、原型、竞品、指标、用户反馈 |
| 作品形式 | GitHub、Demo、README、接口、评测报告 | PRD、竞品分析、原型图、用户流程、模型效果分析 |
| 对用户适配度 | 更适合，因用户是CS背景 | 可以辅投，但不能只讲想法 |
| 短期建议 | 主攻 | 辅投 |

### 3.4 大厂 vs 中小厂/AI原生创业公司

大厂或头部大模型公司更看重：

- 学校背景。
- 算法和工程基础。
- 项目复杂度。
- 实习时长稳定性。
- 系统设计和评测意识。
- 对模型原理的理解。

中小厂/AI原生创业公司更看重：

- 是否能快速做Demo。
- 是否会Dify/Coze/n8n。
- 是否能调API、写脚本、处理数据。
- 是否有GitHub/视频/可演示作品。
- 是否能沟通需求、写文档、推进落地。

结论：用户应优先投递广深中小AI公司、AI原生创业公司、传统企业AI转型岗位、大厂边缘AI应用岗位；不要一开始只冲头部大模型公司核心算法或大厂高门槛AI开发。

## 4. 市场判断和岗位选择

### 4.1 用户更适合的主线

用户当前最适合的主线是：

AI应用开发 / RAG应用 / Agent工作流 / AI工具应用 / 大模型评测与Prompt优化。

不建议主攻：

- 大模型算法研究。
- 预训练。
- SFT/RLHF。
- 强PyTorch算法开发。
- 纯模型部署优化。

原因：

- 用户当前工程基础和项目经验偏弱。
- 短期目标是12周内拿实习offer。
- JD中应用层岗位数量更多，对可展示Demo更友好。
- AI应用开发能利用用户CS背景，同时不要求算法研究能力过强。

### 4.2 找实习概率理性估计

按执行质量估计：

| 情况 | AI方向实习概率估计 |
|---|---|
| 只看教程，项目粗糙，6月底才开始投 | 20%-30% |
| 做出1个可展示RAG项目并正常投递 | 35%-45% |
| 做出2-3个完整项目，有GitHub/Demo/README，持续投递 | 50%-65% |
| 只盯大厂/头部大模型公司AI应用开发 | 10%-20% |
| 广深中小厂/AI原生创业公司/传统企业AI化岗位 | 50%-70% |
| 泛AI岗位，包括AI应用、AI工作流、AI工具、AI训练/评测 | 65%-80% |

这些概率不是保证，只是基于用户背景、岗位样本和市场竞争的理性估计。

### 4.3 AI训练师能否保底

可以作为保底，但必须挑类型。

建议投递的AI训练/评测类岗位：

- 大模型评测实习生。
- Prompt优化实习生。
- RAG数据处理/知识库运营。
- AI产品体验评测。
- Agent测试/评测。
- 语料构建 + Python清洗。

不建议投递的岗位：

- 纯数据标注。
- 内容审核/客服质检。
- 只做复制粘贴Prompt。
- 付费培训后推荐就业。
- 无Python、无评测、无产品参与的岗位。

策略：AI应用开发是主线，6月下旬开始同步投大模型评测/Prompt优化/RAG数据处理作为保底。

## 5. 推荐技术栈优先级

| 优先级 | 技术方向 | 理由 |
|---|---|---|
| S | Python + LLM API + Prompt + RAG | JD最高频，短期能做出作品 |
| S | Agent + Function Calling + LangGraph/Dify | 与2026智能体趋势相关 |
| A | Streamlit/FastAPI + GitHub + README + Demo视频 | 证明工程交付能力 |
| A | SQL/Pandas/文档解析/PDF转Markdown | 很多企业AI落地从数据处理开始 |
| A | Dify/Coze/n8n | 快速做POC，应用岗和产品岗都吃香 |
| B | MCP | 趋势项，适合作为加分项，不是前4周主线 |
| B | 多模态文档RAG | 适合作为第三项目或加分方向 |
| C | LoRA/SFT/RLHF/PyTorch训练 | 短期回报低，不适合当前主线 |

## 6. 12周学习路线总览

总体分阶段：

- 第1-4周：基础补强 + 核心技术栈入门。
- 第5-8周：项目实战，至少完成2个完整项目，最好3个。
- 第9-12周：简历打磨 + 面试冲刺 + 持续投递。

### 第1周：Embedding与向量RAG入门

核心目标：把关键词RAG升级为Embedding + Chroma/FAISS语义检索。

每日时间分配：

- 上午2h：学习Embedding、向量库、RAG流程。
- 下午2h：改造现有LangChain Demo。
- 晚上2h：记录踩坑、整理README。

产出物：本地文件问答RAG v0。

对应JD要求：RAG知识库、Python、Prompt、LLM API。

### 第2周：RAG质量优化

核心目标：掌握chunk、metadata、top_k、rerank、引用来源、评测集。

每日时间分配：

- 上午2h：学习RAG评测与检索优化。
- 下午2h：做20-50条问答测试集。
- 晚上2h：对比关键词检索 vs 向量检索。

产出物：RAG评测表 + 优化报告。

对应JD要求：模型评测、RAG链路优化、技术文档。

### 第3周：Web化与工程化

核心目标：把RAG做成可演示应用。

每日时间分配：

- 上午2h：FastAPI/Streamlit、HTTP/JSON。
- 下午2h：开发上传文档、问答、引用展示。
- 晚上2h：Git、环境变量、异常处理、日志。

产出物：可运行Demo + GitHub仓库。

对应JD要求：Python后端、API、GitHub、完整项目经验。

### 第4周：AI产品与低代码工作流

核心目标：补Dify/Coze/n8n和产品表达能力。

每日时间分配：

- 上午2h：Dify/Coze搭知识库和工作流。
- 下午2h：学习PRD、竞品分析、Figma/Axure基础。
- 晚上2h：写项目1产品说明和架构图。

产出物：Dify版RAG Demo + 一页产品说明。

对应JD要求：AI工作流、产品思维、文档写作。

### 第5周：项目1完整开发

核心目标：做“AI求职知识库与岗位匹配助手”。

每日时间分配：

- 上午2h：整理Boss JD、个人简历字段、匹配指标。
- 下午2h：实现JD解析、能力标签、匹配问答。
- 晚上2h：优化Prompt和结果格式。

产出物：项目1核心功能完成。

对应JD要求：RAG、知识库、Prompt、业务AI化。

### 第6周：项目1打磨与上线

核心目标：让项目1达到简历级。

每日时间分配：

- 上午2h：加评测、错误处理、引用来源。
- 下午2h：写README、部署说明、截图。
- 晚上2h：录3分钟Demo视频，准备简历描述。

产出物：GitHub + Demo视频 + 项目复盘文章。

对应JD要求：可展示AI作品、GitHub、评测文档。

### 第7周：项目2 Agent入门

核心目标：掌握Agent工具调用和工作流编排。

每日时间分配：

- 上午2h：学习ReAct、Function Calling、LangGraph。
- 下午2h：实现任务拆解、文件读取、SQL查询等工具。
- 晚上2h：用Dify/Coze复刻同一流程。

产出物：办公Agent v0。

对应JD要求：Agent、工具调用、AI工作流、自动化提效。

### 第8周：项目2工程化 + MCP小实验

核心目标：让Agent具备可解释流程和可扩展工具。

每日时间分配：

- 上午2h：学习MCP基本概念与工具接口。
- 下午2h：封装FastAPI工具或简易MCP服务。
- 晚上2h：写Agent流程图、失败案例和改进方案。

产出物：项目2上线版 + MCP/工具调用说明。

对应JD要求：MCP、Function Call、Agent架构、技术文档。

### 第9周：项目3文档解析RAG

核心目标：做PDF/Word转Markdown + 文档RAG。

每日时间分配：

- 上午2h：学习文档解析、Markdown结构化、表格处理。
- 下午2h：实现上传、解析、分块、入库。
- 晚上2h：处理异常文档和中文检索问题。

产出物：多格式文档RAG v0。

对应JD要求：非结构化文档处理、RAG、数据处理。

### 第10周：项目3评测与部署

核心目标：补齐评测、看板、部署，让项目更有区分度。

每日时间分配：

- 上午2h：学习召回率、命中率、延迟、成本指标。
- 下午2h：做Streamlit/FastAPI评测看板。
- 晚上2h：Docker/Linux部署、README完善。

产出物：项目3完整版 + 评测报告。

对应JD要求：模型评测、部署、Linux/Docker、工程化落地。

### 第11周：简历与面试冲刺

核心目标：把项目转成HR和面试官能看懂的证据。

每日时间分配：

- 上午2h：刷Python、SQL、基础算法。
- 下午2h：复盘3个项目的技术问题。
- 晚上2h：改简历、Boss主页、模拟面试。

产出物：一页简历 + Boss资料 + 项目答辩稿。

对应JD要求：Python、SQL、项目经验、沟通表达。

### 第12周：集中投递与迭代

核心目标：高频投递、复盘面试、快速补短板。

每日时间分配：

- 上午2h：投递与Boss沟通。
- 下午2h：针对JD微调简历和项目描述。
- 晚上2h：面试复盘、查漏补缺、继续刷题。

产出物：100-200个有效沟通、面试记录表、最终作品集。

对应JD要求：主动推进、快速迭代、可展示作品。

## 7. 三个实战项目

### 项目1：AI求职知识库与岗位匹配助手

方向：RAG + 求职场景。

技术栈：

- Python。
- LangChain或LlamaIndex。
- Chroma或FAISS。
- DeepSeek/Qwen API。
- Streamlit。

功能：

- 导入JD和个人简历文本。
- 对JD做标签抽取。
- 构建岗位知识库。
- 支持简历匹配、能力差距分析、JD摘要、学习建议。
- 输出引用来源。
- 做一组评测问题。

对应JD要求：

- RAG。
- 知识库。
- Prompt。
- AI应用Demo。
- GitHub作品。

简历包装：

“基于LangChain和Chroma构建岗位JD知识库，支持简历匹配、能力差距分析和岗位问答；设计Prompt模板和评测集，支持引用来源展示，并通过Streamlit完成可视化Demo。”

### 项目2：企业办公Agent工作流助手

方向：Agent + 自动化工作流。

技术栈：

- LangGraph或LangChain Agent。
- Function Calling。
- Dify/Coze。
- FastAPI。
- SQLite。

功能：

- 周报生成。
- 资料归档。
- 任务拆解。
- 文件读取。
- SQL查询。
- 工具调用轨迹展示。

对应JD要求：

- Agent。
- 工具调用。
- 工作流编排。
- 自动化提效。
- 业务AI化。

简历包装：

“实现面向办公场景的Agent工作流，支持任务拆解、工具调用、文件读取和结构化输出；沉淀可复用Prompt模板，并用Dify复刻流程完成低代码POC。”

### 项目3：多模态文档RAG与评测平台

方向：非结构化文档处理 + RAG评测。

技术栈：

- Python。
- PDF/Word解析工具。
- Markdown结构化。
- Chroma/FAISS。
- Rerank可选。
- Streamlit/FastAPI。
- Docker可选。

功能：

- PDF/Word转Markdown。
- 文档分块。
- 向量化入库。
- 问答。
- 来源引用。
- 召回率/延迟/成本评测看板。

对应JD要求：

- 文档解析。
- RAG。
- 数据处理。
- 评测。
- 部署。

简历包装：

“实现多格式文档解析与RAG问答平台，支持PDF/Word转Markdown、向量检索、来源引用与评测看板；对比不同chunk_size/top_k参数对回答质量的影响。”

## 8. 学习方法建议

用户之前在Cursor中的学习方式：

- 让AI读取LangChain官方文档。
- AI直接给出完整day1.py。
- 用户截图代码并照着敲。
- Day1做了深入理解、让AI出题检查并生成总结。
- Day2跟着做Embedding/RAG，但理解不深，没有总结。

问题：

- 容易变成照抄代码。
- Day2后理解闭环断掉。
- 没有稳定的总结、复盘、测试和改造。

建议的新学习闭环：

每一个小步骤都必须经历：

1. AI给最小步骤。
2. 用户运行。
3. 用户解释代码。
4. AI出题检查。
5. 用户回答。
6. AI判断是否能进入下一步。
7. 用户做一个小改造。
8. 用户写summary.md。

每个Day结束必须留下：

- `summary.md`：今天学了什么、掌握了什么、还不懂什么。
- `questions.md`：AI出的题和用户答案。
- `blockers.md`：当天卡点。
- `next_steps.md`：下一步。

不要让AI一次性给完整项目。更合适的提示词：

```text
你是我的LangChain学习带教老师。

我的背景：
- 计算机本科大三
- Python基础一般
- 已学过LLM API调用和Prompt模板
- Day2的Embedding/RAG理解不深
- 目标是12周内做出能写进简历的RAG/Agent项目

规则：
1. 不要一次性给完整项目代码。
2. 每次只推进一个小步骤。
3. 每一步必须包含：本步目标、为什么这么做、最小代码、运行命令、预期输出、常见报错、必须掌握的知识点。
4. 每步结束后出5个检查题：概念题、代码解释题、参数变化题、报错排查题、小改造题。
5. 等我回答后，你判断我是否能进入下一步。
6. 如果我贴报错，只给最小修改方案，不要重写整个文件。
```

## 9. Cursor、Claude终端、Codex5.3的分工

用户计划：

- 在Cursor中使用接入DeepSeek-V4-Pro的Claude终端作为主模型。
- Cursor免费额度中的Codex5.3作为关键问题救火和阶段审查。

推荐分工：

| 任务 | 主模型 |
|---|---|
| 日常学习计划 | DeepSeek-Claude终端 |
| 官方文档学习后的日常讲解 | DeepSeek-Claude终端 |
| 一步步搭Demo | DeepSeek-Claude终端 |
| 代码逐行解释 | DeepSeek-Claude终端 |
| 出题检查理解 | DeepSeek-Claude终端 |
| 学习总结 | DeepSeek-Claude终端 |
| 复杂报错定位 | 先DeepSeek-Claude，卡住20分钟再Codex5.3 |
| 项目结构设计 | Codex5.3 |
| 代码质量审查 | Codex5.3 |
| 阶段验收 | Codex5.3 |
| 简历项目包装 | Codex5.3 |

关键原则：

- DeepSeek-Claude负责80%的日常学习。
- Codex5.3负责20%的关键审查、复杂debug、项目升级、简历包装。
- 不要把Codex5.3用在普通概念解释和日常总结上。

## 10. 官方文档读取问题的解决方案

如果Claude终端不能直接读取LangChain官方文档链接，可采用以下方案。

### 方案1：接入LangChain官方MCP

在Claude Code终端执行：

```powershell
claude mcp add --transport http docs-langchain https://docs.langchain.com/mcp
```

若希望所有项目可用：

```powershell
claude mcp add --transport http docs-langchain --scope user https://docs.langchain.com/mcp
```

然后在Claude终端输入：

```text
/mcp
```

确认`docs-langchain`已连接。

之后可要求Claude：

```text
请通过docs-langchain MCP查询LangChain Python中关于Chat models、Prompt templates、RAG、Text splitters、Vector stores的官方文档。
不要一次性教完整项目。请先告诉我完成Day1最小Demo必须读哪些页面，然后只带我完成第一步。
```

### 方案2：让Cursor Agent/Codex5.3做文档搬运工

让Codex5.3读取官方文档并整理成本地Markdown：

```text
请读取LangChain官方文档中适合初学者完成Python版RAG Demo的页面。
只做文档整理，不教我写代码。

请整理成本地Markdown文件：
docs/langchain/day1_llm_prompt.md
docs/langchain/day2_text_splitter.md
docs/langchain/day3_embedding_vectorstore.md
docs/langchain/day4_rag_chain.md

每个文件包含：
1. 官方文档链接
2. 核心概念
3. 最小代码片段
4. 初学者容易误解的点
5. 今日练习任务
```

然后让DeepSeek-Claude终端读取本地Markdown继续教学。

推荐最终项目结构：

```text
stuLang_out/
├─ CLAUDE.md
├─ docs/
│  └─ langchain/
│     ├─ day1_llm_prompt.md
│     ├─ day2_basic_rag.md
│     ├─ day3_embedding_chroma.md
│     └─ day4_streamlit.md
├─ notes/
│  ├─ learning_log.md
│  ├─ blockers.md
│  └─ next_steps.md
└─ src/
```

在`CLAUDE.md`中写：

```text
你是我的LangChain学习带教老师。

学习规则：
1. 优先读取docs/langchain/下的官方文档笔记。
2. 不要一次性给完整项目。
3. 每次只推进一个小步骤。
4. 每步结束后出5道检查题。
5. 如果遇到不确定内容，提醒我用Codex5.3或Cursor Agent核对官方文档。
6. 每天结束更新notes/learning_log.md和notes/next_steps.md。
```

## 11. 求职时间线

| 时间 | 动作 |
|---|---|
| 5月中旬-5月底 | 主攻LangChain、RAG、Embedding、Chroma，完成第一个RAG Demo |
| 6月1日-6月20日 | 小规模试投，每天5-10个，测试简历反馈 |
| 6月21日-7月10日 | 海投高峰，每天20-30个Boss沟通 |
| 7月11日-7月31日 | 收缩精投，重点跟进面试、内推、复盘 |
| 8月 | offer选择、补材料、准备入职 |

若6月25日后AI应用开发反馈较少，应同步投递：

- 大模型评测实习生。
- Prompt优化实习生。
- RAG数据处理。
- AI工具应用。
- AI产品实习。
- AI训练师中偏评测/Prompt/知识库方向的岗位。

## 12. 简历优化方向

用户原经历应这样重写：

| 原经历 | 改写方向 |
|---|---|
| Streamlit + DeepSeek聊天助手 | 基于DeepSeek API实现Web聊天助手，支持环境变量配置、Prompt模板、前端交互 |
| Python爬虫 | 使用Python完成数据采集、清洗与结构化存储，可支撑知识库构建 |
| C++链表课设 | 掌握数据结构、面向对象设计和基础工程实现 |
| 蓝桥杯省二 | 具备算法与编程基础，能适应技术面笔试 |
| LangChain Day1/Day2 | 已完成LLM调用、LCEL、文本切块、基础RAG、Embedding、Chroma向量检索 |

技能关键词建议：

`Python`、`LangChain`、`RAG`、`Agent`、`Prompt Engineering`、`DeepSeek/Qwen API`、`Chroma/FAISS`、`FastAPI/Streamlit`、`Dify/Coze`、`Git`、`SQL`、`Linux`、`MCP`。

## 13. 面试准备重点

技术面常问：

- RAG完整流程。
- Embedding是什么。
- 向量库做什么。
- chunk_size和chunk_overlap如何影响检索。
- top_k如何选择。
- Prompt如何减少幻觉。
- Agent和普通Chain有什么区别。
- Function Calling是什么。
- 如何做来源引用。
- 如何评估RAG效果。
- 项目中遇到的具体报错和解决过程。

笔试：

- Python基础。
- 字符串、数组、哈希、链表、树。
- 简单动态规划。
- SQL查询。
- HTTP/JSON基础。

产品面：

- PRD结构。
- 用户需求拆解。
- 竞品分析。
- 指标设计。
- 模型效果评估。
- AI功能边界与安全风险。

## 14. Boss直聘打招呼模板

```text
你好，我是27届计算机本科生，正在找AI应用开发/AI工作流方向实习。

我已完成DeepSeek API、LangChain RAG、Dify工作流相关项目，正在做“岗位JD知识库匹配助手”和“办公Agent自动化助手”，可提供GitHub和Demo视频。

我每周可到岗4-5天，能连续实习3个月以上。想请问这个岗位是否更看重RAG/Agent项目经验？方便的话我可以发作品链接给您参考。
```

## 15. 资源清单

| 类型 | 资源名称 | 适用阶段 | 免费/付费 |
|---|---|---|---|
| 视频课程 | B站黑马/尚硅谷Python基础 | 第1周补基础 | 免费 |
| 视频课程 | 吴恩达Prompt Engineering/LangChain课程 | 第1-4周 | 多数免费 |
| 视频课程 | Datawhale AI Agent/RAG教程 | 第1-8周 | 免费 |
| 开源项目 | LangChain/LangGraph | 第1-8周 | 免费 |
| 开源项目 | LlamaIndex | 第2-6周 | 免费 |
| 开源项目 | Dify | 第4-8周 | 免费 |
| 开源项目 | RAGFlow/FastGPT/QAnything | 第6-10周 | 免费 |
| 开源项目 | Chroma/FAISS/Milvus | 第1-10周 | 免费 |
| 文档 | DeepSeek API文档、Qwen API文档 | 全阶段 | 免费 |
| 文档 | LangChain官方文档 | 全阶段 | 免费 |
| 社群/平台 | ModelScope、飞桨AI Studio、阿里天池 | 项目/比赛 | 免费 |
| 社群/平台 | GitHub、牛客、实习僧、Boss直聘 | 投递阶段 | 免费 |
| 社群/平台 | Datawhale、掘金、CSDN、知乎AI专题 | 全阶段 | 免费 |

## 16. 给后续模型的关键提醒

请后续模型不要盲目鼓励用户，也不要把用户规划到算法岗。用户当前最需要的是：

1. 稳定完成LangChain/RAG基础。
2. 每日形成代码 + 理解 + 总结 + 改造闭环。
3. 尽快做出第一个可展示RAG项目。
4. 6月开始边学边投，不要等完全准备好。
5. 主攻AI应用开发，辅投AI工作流、AI工具应用、AI产品、大模型评测/Prompt优化。
6. 使用Codex5.3时应节省额度，只做阶段审查、复杂debug和项目包装。
7. 不要让用户陷入“阅读完整官方文档”或“追逐最新模型名词”的陷阱。
8. 判断用户是否掌握，不看是否跑通代码，而看是否能解释、复现、改造、排错。

最终一句话：

用户的最优路径是“用12周做出2-3个可展示AI应用项目，形成GitHub/Demo/README/评测报告，然后广泛投递AI应用开发、AI工作流、AI产品和大模型评测相关实习”。不是追求成为算法研究员，而是先成为能把AI能力落地到业务流程中的AI应用实习生。
