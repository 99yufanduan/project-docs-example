# 使用说明

从仓库根目录运行以下命令：

```bash
python3 check_report.py /path/to/report.json
```

正常结果以 JSON 写到标准输出。退出码 `0` 表示通过，`1` 表示指标未通过，`2` 表示命令参数或输入无效。输入错误写到标准错误。可用重定向保存检查结果：

```bash
python3 check_report.py examples/passing.json > /tmp/calibration-check.json
```

- [第一次运行](docs/getting-started/quickstart.md)
- [检查自己的报告](docs/guides/checking-a-report.md)
- [CLI 与报告格式](docs/reference/report-interface.md)
