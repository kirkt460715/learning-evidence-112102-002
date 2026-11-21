# 记录格式

查证记录以 id、claim、source、excerpt、student_action、judgement 表示论断、来源标识、摘录和学生动作。source 为 missing 时没有来源材料。

记录以 UTF-8 JSON 保存，顶层包含 dataset 和 records。每条记录的 id 在文件中唯一。`fixtures/records.json` 中的例子用于说明输入字段和状态取值。
