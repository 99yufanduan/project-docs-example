# CLI 与报告格式

调用形式为 `python3 check_report.py REPORT`。`REPORT` 是 UTF-8 编码的 JSON 文件路径。根节点为对象，其中 `metrics` 保存测量值，`limits` 保存同名上限。两个对象均要求以下字段。

| 键 | 含义 | 单位 |
|---|---|---|
| `reprojection_rmse_px` | 重投影误差的均方根 | 像素 |
| `epipolar_mean_px` | 平均极线误差 | 像素 |

值须为非负有限数字。程序只读取表中两项，其他字段可作为上游元数据。

输出为 JSON。`passed` 表示整体结果，`checks` 按指标键保存 `value`、`limit` 和逐项 `passed`。

| 退出码 | 含义 | 输出 |
|---|---|---|
| `0` | 两项都通过 | 标准输出包含检查 JSON |
| `1` | 至少一项超限 | 标准输出包含检查 JSON |
| `2` | 命令参数无效，或报告无法读取或校验 | 标准错误包含说明 |
