# Requirement Review Workflow

## Step 1 — Understand Context

读取：

- context/project-context.md
- rules/review-rules.md

---

## Step 2 — Read Requirement

读取目标需求。

识别：

- 角色
- 主流程
- 输入
- 输出
- 状态
- 数据
- 权限

---

## Step 3 — Identify Ambiguities

寻找：

- 未定义业务规则
- 状态流转缺失
- 权限边界缺失
- 数据模型缺失
- 流程闭环问题

---

## Step 4 — Prioritize

按照 review-rules.md 分级。

---

## Step 5 — Generate Review

生成标准评审报告。

---

## Step 6 — Verify

调用：

tools/check_review.py

检查输出。

---

## Step 7 — Finish

只有验证通过后，才能宣布任务完成。