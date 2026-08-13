# ai-product-copilot
AI copilot for product managers: generate structured requirement docs from a business description, then analyze them to identify gaps and generate actionable questions.

## Architecture

```
Context
→ Rules
→ Workflow
→ Tools
→ Evaluation
```

## Goal

让Agent帮助产品经理发现：

- 需求歧义
- 缺失业务规则
- 状态流转问题
- 权限问题
- 数据模型风险

## Cost Strategy

确定性任务交给程序。

LLM只处理需要理解和判断的任务。

## Verification

所有输出必须经过自动检查。

## Current Version

V1.0
