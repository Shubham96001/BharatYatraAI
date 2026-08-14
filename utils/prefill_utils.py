def normalize_list(items):
    """Filter and join a list of strings into a comma-separated, cleaned phrase."""
    if not items:
        return ""
    out = []
    for it in items:
        if not it:
            continue
        s = str(it).strip()
        if s:
            out.append(" ".join(s.split()))
    return ", ".join(out)


def build_prefill_prompt(name: str, data: dict, is_country: bool = False) -> str:
    """Construct a normalized prefill prompt for the planner."""
    best_time = (data.get("best_time") or "").strip()
    highlights = normalize_list(data.get("highlights", []))
    capital = (data.get("capital") or "").strip()
    budget = (data.get("budget") or "").strip()

    if is_country:
        parts = [f"Plan a trip to {name}"]
        if best_time:
            parts.append(f"best time: {best_time}")
        if highlights:
            parts.append(f"highlights: {highlights}")
    else:
        parts = [f"Plan a trip to {name}"]
        if capital:
            parts.append(f"capital: {capital}")
        if best_time:
            parts.append(f"best time: {best_time}")
        if budget:
            parts.append(f"budget: {budget}")
        if highlights:
            parts.append(f"highlights: {highlights}")

    # Join with periods for clearer separation
    prompt = ". ".join([p for p in parts if p])
    return prompt
