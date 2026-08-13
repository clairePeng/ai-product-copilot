# Requirement Generation Workflow

## Step 1 — Read Business Description

读取用户提供的业务描述。

可能来自：

- 用户直接粘贴的文本
- 用户指定的文件路径

## Step 2 — Understand Context

读取：

- docs/project-context.md
- rules/generation-rules.md

## Step 3 — Generate PRD

按照 `prompts/requirement-generation.md` 中定义的结构，生成结构化业务需求文档。

## Step 4 — Save Requirement

保存到 `test-data/requirementNNN.md`。

编号规则：在 `test-data/requirement*.md` 现有最大编号基础上递增，3位数字补零。

## Step 5 — Trigger Review

自动触发 `workflows/requirement-review.md`，对刚生成的需求文件执行完整评审流程。

## Step 6 — Verify

调用：

tools/check_review.py

检查生成的评审报告是否结构完整。

## Step 7 — Finish

只有需求文档已保存、评审报告已生成并通过验证后，才向用户报告：

- 生成的需求文档路径
- 对应的评审报告路径
