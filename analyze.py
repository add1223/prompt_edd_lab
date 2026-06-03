import json
from error_analysis import summarize_failures, suggest_prompt_changes

with open("outputs/eval_report.json", "r", encoding="utf-8") as f:
    report = json.load(f)
results = report["results"]
summary = summarize_failures(results)
print("错误统计：", summary)
suggestions = suggest_prompt_changes(summary)
for s in suggestions:
    print("-", s)
