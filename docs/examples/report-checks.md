# 通过与超限案例

从仓库根目录运行以下两条命令。每条命令之后可用 `echo $?` 查看退出码。

```bash
python3 check_report.py examples/passing.json
python3 check_report.py examples/failing.json
```

| 报告 | 预期输出 | 退出码 |
|---|---|---|
| [passing.json](../../examples/passing.json) | 总体通过。平均极线误差为 0.40 px，等于阈值。 | `0` |
| [failing.json](../../examples/failing.json) | 总体未通过。平均极线误差为 0.65 px，超过 0.40 px。 | `1` |

若程序可以读取文件但缺少必需字段，会输出字段错误并返回 `2`。完整契约见[接口参考](../reference/report-interface.md)。
