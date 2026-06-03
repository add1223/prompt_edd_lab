from rubric import REQUIRED_SECTIONS


def check_required_sections(output: str) -> list[str]:
    errors = []
    for section in REQUIRED_SECTIONS:
        if section not in output:
            errors.append(f"missing section: {section}")
    return errors


def check_min_length(output: str, min_chars: int = 40) -> list[str]:
    if len(output.strip()) < min_chars:
        return ["output is too short"]
    return []


def check_forbidden_points(output: str, forbidden_points: list[str]) -> list[str]:
    errors = []
    content_start = output.find("回复正文：")
    notes_start = output.find("注意事项：")
    negation_words = ["不", "否", "无", "没", "非", "不能", "不可", "无法"]
    
    if content_start >= 0:
        if notes_start > content_start:
            content_text = output[content_start:notes_start]
        else:
            content_text = output[content_start:]
        
        for phrase in forbidden_points:
            if phrase in content_text:
                idx = content_text.find(phrase)
                has_negation = False
                for neg in negation_words:
                    neg_idx = content_text.rfind(neg, 0, idx)
                    if neg_idx >= 0:
                        between = content_text[neg_idx+len(neg):idx].strip()
                        if len(between) <= 5:
                            has_negation = True
                            break
                if not has_negation:
                    errors.append(f"forbidden phrase appears: {phrase}")
    return errors


def run_static_checks(output: str, forbidden_points: list[str]) -> list[str]:
    errors = []
    errors.extend(check_required_sections(output))
    errors.extend(check_min_length(output))
    errors.extend(check_forbidden_points(output, forbidden_points))
    return errors
