# Day1 复习问答整理（DeepSeek / Claude Code 会话）

本文档根据终端会话记录整理：**题目**、**你的回答**、**模型的纠正与完整点评**。会话中模型侧为 Claude Code（计费显示 deepseek-v4-pro），下文按你的习惯统称「DeepSeek 复习」。

---

## 一、复习 Step 1：模型基础调用（五道检查题）

> 终端中提示「请先创建 `review_step1.py` 并运行」，随后列出本题；**本次终端记录里未见你对本组五题的作答**（会话在 `exit` 后结束）。题目原文保留便于补答。

1. **概念题**：`model.invoke()` 的入参可以是一个字符串，也可以是什么？查阅 Day1 代码，`step2_prompt_template` 里传给 `chain.invoke()` 的是什么类型？

2. **代码解释题**：`temperature=0.2` 和 `temperature=0.8` 有什么区别？什么时候用低的，什么时候用高的？

3. **参数变化题**：若把 `model="deepseek-chat"` 改成 `model="deepseek-v4-flash"`，会发生什么？（提示：Day2 代码里用的是哪个？）

4. **报错排查题**：若运行时看到 `openai.APIError: Error code: 401 - Invalid API Key`，问题可能出在哪里？请说出至少 2 种可能原因。

5. **小改造题**：修改代码，让模型用英文回答同一个问题。需要改什么？请写出改动后的关键代码片段。

---

## 二、进入 Day2 前的 Day1 五道检查题（含作答与点评）

### 题目

1. **概念题**：`RunnablePassthrough()` 在 Day1 的 `step3_rag_demo` 里起什么作用？如果删掉它，代码会怎样？

2. **代码解释题**：下面代码中，`|` 和 `{}` 分别是什么意思？

   ```python
   rag_chain = (
       {"context": retriever, "question": RunnablePassthrough()}
       | prompt
       | model
       | StrOutputParser()
   )
   ```

3. **参数变化题**：`RecursiveCharacterTextSplitter` 的 `chunk_overlap` 从 20 改成 80 会发生什么？什么情况下加大 overlap 是有意义的？

4. **报错排查题**：运行 Day1 代码时看到 `ValueError: 未检测到 DEEPSEEK_API_KEY`，但已创建 `.env` 并放了 key。可能的原因是什么？（提示：对比 `day1.py` 和 `day1_test.py`）

5. **小改造题**：`simple_retrieve` 目前只按关键词数量打分。若要让它也能匹配「同义词」（例如「大模型」和「LLM」），有哪两种思路？（不要求写代码，说思路即可）

---

### 你的回答（原文整理）

| 题号 | 你的回答（要点） |
|------|------------------|
| 1 | 将文档内容进行切分后检索；文档内容未切分，代码会无法运行报错。 |
| 2 | `\|` 是管道；`{}` 是字典。 |
| 3 | `chunk_overlap` 表示相邻文本共享切块的大小，保持文本一致性；数字越大，共享越大。 |
| 4 | `load_dotenv()` 的作用：可以读取 `.env` 里配置好的 API key。 |
| 5 | (1) 用向量比较，语义向量化，向量相近说明语义相近；(2) 同时比较两者关键词数量，数量相近说明语义相近。 |

---

### 模型的纠正与逐题回答

#### 第 1 题 — 需要纠正

- **纠正**：你把 `RunnablePassthrough()` 和 `load_docs()` 搞混了。`RunnablePassthrough()` 出现在  
  `{"context": retriever, "question": RunnablePassthrough()}`  
  它的作用是：**把用户输入原样透传给 `question` 字段**。当调用 `rag_chain.invoke("LangChain 的核心能力有哪些？")` 时，这句话会同时给 `retriever`（检索）和 `question`（最终问题）。**删掉它则 `question` 收不到值**。
- **补充**：你所说的「切分文档」是 `load_docs()` 做的事，不是 `RunnablePassthrough`。

#### 第 2 题 — 对但不完整

- **`|`**：你答「管道」没错，需明确为 **LangChain 的 LCEL 管道操作符**，与 Linux shell 的 pipe 类似：左输出接右输入。
- **`{}`**：确是字典，关键点在于：**字典里每个 value 都是一个 Runnable**，LangChain 会**并行**执行它们，最后拼成一个 dict 传给下一环节。

#### 第 3 题 — 基本正确，补充场景

- **肯定**：「文本一致性」的说法对。
- **补充**：当文档是**法律合同或学术论文**时，关键术语的定义可能恰好在 chunk 边界被切断；**增大 `chunk_overlap` 有助于避免丢失上下文**。

#### 第 4 题 — 完全正确

- **确认**：`load_dotenv()` 会读取 `.env` 并注入 `os.environ`；**`day1.py` 缺少该行时，即使存在 `.env` 也读不到 key**。

#### 第 5 题 — 思路 1 正确，思路 2 不对

- **思路 1（向量化）**：正确，正是 Day2 方向，也是正解。
- **思路 2 的纠正**：「比较关键词数量」本就是 `simple_retrieve` 在做的事，**解决不了「大模型」与「LLM」的匹配问题**。
- **更合适的第二种思路**：建立**同义词词典**，检索前把问题中的词**替换为同义词再匹配**。

---

### 总体判断（模型原文要点）

- Day1 **步骤 1、步骤 2**掌握不错；**`RunnablePassthrough` 与 LCEL 链的构建逻辑**仍需巩固。
- **不影响进入 Day2**；Day2 会在更多链的实践中加深理解。
- **结论**：可以进入 Day2。

---

## 三、说明

- 整理来源：本地终端输出（`stuLangchain` 目录下 `claude` 会话片段）。
- 若你之后补答「复习 Step 1」五题，可把答案追加到本文档第一节下方，便于统一归档。
