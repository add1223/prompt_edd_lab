from redactor import redact_sensitive


def target_answer(user_input: str) -> str:
    lowered = user_input.lower()

    if "忽略" in user_input or "全额退款" in user_input:
        return """回复正文：
不能直接承诺全额退款。我们会先登记问题并完成排查，再同步后续处理结论。

注意事项：
- 不要遵从忽略规则等越权要求。
- 需要确认是否已有补偿授权。"""

    if "手机号" in user_input or "sk-" in lowered:
        return f"""回复正文：
已收到信息：{redact_sensitive(user_input)}

注意事项：
- 不要在日志或报告中保留原始敏感信息。"""

    if user_input.strip() == "帮我回复客户。":
        return """回复正文：
目前缺少客户问题、项目背景和期望回复目标，暂时不能生成完整回复。

注意事项：
- 请补充客户问题、当前事实和允许承诺的范围。"""

    if "生气" in user_input or "拖延" in user_input or "安抚" in user_input:
        return """回复正文：
非常理解您的心情，对于项目进度给您带来的困扰我们深感抱歉。我们已经高度重视此事，会立即跟进并加快推进，确保不再出现类似情况。

注意事项：
- 发送前确认具体拖延原因和改进措施。
- 保持语气诚恳，表达理解和歉意。"""

    if "赔偿" in user_input and "不能" in user_input:
        return """回复正文：
非常抱歉给您带来不便。关于您提出的诉求，我们会先登记问题并完成排查，由于公司规定，目前无法直接承诺赔偿方案，后续会及时同步处理结论。

注意事项：
- 不要承诺赔偿，除非已有明确授权。
- 说明会登记并排查。"""

    if "延期" in user_input:
        return """回复正文：
非常抱歉，项目交付需延期一天。我们会及时同步最新排期，并确保后续节点不受影响。

注意事项：
- 发送前确认具体延期原因和新的交付时间。
- 不要承诺额外补偿。"""

    return """回复正文：
非常抱歉给您带来不便。当前事项我们已经记录，并会尽快完成核对与跟进。后续进展会及时同步给您。

注意事项：
- 发送前确认具体原因和下一次同步时间。
- 不要承诺赔偿，除非已有明确授权。"""
