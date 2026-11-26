#!/usr/bin/env python3
"""Check a stereo calibration report against its configured limits."""

import argparse
import json
import math
import sys
from pathlib import Path


METRICS = ("reprojection_rmse_px", "epipolar_mean_px")


def read_values(report: dict, section: str) -> dict[str, int | float]:
    values = report.get(section)
    if not isinstance(values, dict):
        raise ValueError(f"{section} 必须是对象")

    checked = {}
    for metric in METRICS:
        value = values.get(metric)
        if type(value) not in (int, float) or value < 0:
            raise ValueError(f"{section}.{metric} 必须是非负有限数值")
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError(f"{section}.{metric} 必须是非负有限数值")
        checked[metric] = value
    return checked


def check_report(path: Path) -> dict:
    report = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(report, dict):
        raise ValueError("报告根节点必须是对象")

    metrics = read_values(report, "metrics")
    limits = read_values(report, "limits")
    checks = {
        name: {"value": metrics[name], "limit": limits[name], "passed": metrics[name] <= limits[name]}
        for name in METRICS
    }
    return {"passed": all(check["passed"] for check in checks.values()), "checks": checks}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="Calibration report JSON file")
    args = parser.parse_args()

    try:
        result = check_report(args.report)
    except (OSError, ValueError) as error:
        print(f"无法读取有效报告 {args.report}：{error}", file=sys.stderr)
        return 2

    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
