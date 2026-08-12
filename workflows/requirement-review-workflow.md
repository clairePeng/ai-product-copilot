# Requirement Review Workflow

## Purpose

将一份业务需求文件转换为结构化的需求评审报告。

---

## Input

输入：

一个 Markdown 格式的业务需求文件。

例如：

test-data/requirement-001.md

---

## Step 1 — Read

读取：

1. 目标需求文件
2. AGENTS.md
3. prompts/requirement-review.md

不得修改原始需求文件。

---

## Step 2 — Understand

识别需求中的：

- 业务对象
- 业务角色
- 核心业务动作
- 主流程
- 已明确的业务规则
- 已明确的状态
- 已明确的权限
- 已明确的数据

不要主动补充需求没有提供的业务事实。

---

## Step 3 — Review

按照 Product Review Framework V1.0 检查：

1. Business Rules
2. State
3. Role & Responsibility
4. Permission
5. Data & Audit
6. Exception & Closure

只提出有证据支持的问题。

---

## Step 4 — Prioritize

将问题分为：

### P0

不确认就无法安全设计核心：

- 业务逻辑
- 状态机
- 责任模型
- 权限模型
- 数据模型

### P1

重要，但不会立即阻塞核心设计。

### P2

可以在设计或开发阶段进一步确认的问题。

不得为了覆盖维度而人为制造问题。

---

## Step 5 — Produce

生成：

1. 需求摘要
2. P0问题
3. P1问题
4. P2问题
5. 核心风险 Top 3
6. 最应该问业务方的5个问题
7. 评审结论

---

## Step 6 — Save

将结果保存到：

review-results/

文件名：

`<原需求文件名>-review.md`

例如：

`requirement-001-review.md`

---

## Step 7 — Verify

生成文件后检查：

- 是否遗漏P0问题
- 是否存在无证据支持的问题
- 是否修改了原始需求
- 输出格式是否符合评审规则
- P0是否真正影响核心设计

---

## Output

最终输出：

一个结构化 Markdown 评审报告。

## Step 7 — Automated Verification

完成评审报告后，使用：

`tools/check_review.py`

进行机械检查。

检查：

1. 原始需求文件是否存在
2. 评审报告是否存在
3. 报告是否包含规定章节
4. 报告字符数

如果检查失败：

- 不得直接宣布任务完成；
- 修正报告后重新检查。

如果检查通过：

- 才能向用户报告任务完成。