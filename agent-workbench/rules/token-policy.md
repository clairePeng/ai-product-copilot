# Token Policy

## LLM First Principle

LLM只处理需要理解、判断、生成的任务。

## Prefer Tools

以下任务优先交给程序：

- 文件检查
- 格式检查
- 字段检查
- 统计
- 重复检测
- 状态检查

## Avoid Duplicate Calls

如果已有有效结果：

默认不重复调用LLM。

只有以下情况允许重新调用：

- 验证失败
- 规则变化
- 用户明确要求
- 原需求发生变化