# Requirement Review Agent — Acceptance Criteria

## AC01 — 自动读取规则

用户只提供需求文件路径时，Agent能够自动找到并读取项目评审规则。

## AC02 — 自动执行Workflow

Agent能够按照Requirement Review Workflow执行任务。

## AC03 — 不修改原始需求

评审过程中不得修改原始需求文件。

## AC04 — 输出结构稳定

报告必须包含：

- 需求摘要
- P0
- P1
- P2
- Top 3风险
- 5个业务问题
- 评审结论

## AC05 — P0有依据

P0问题必须能够说明为什么会影响核心设计。

## AC06 — 不制造业务事实

不得把行业经验或AI推测描述成已经确定的需求事实。

## AC07 — 自动保存报告

评审完成后自动生成对应的review-results文件。

## AC08 — 新需求可迁移

Agent能够对没有见过的新业务需求执行同一套评审框架。

## AC09 — 严重不完整需求能够识别

面对信息极少的需求，Agent应该识别核心缺失，而不是为了凑数量制造大量低价值问题。