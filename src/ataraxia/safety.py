from dataclasses import dataclass


@dataclass
class SafetyResult:
    safe: bool
    reason: str = ""


def validate_response(response: str) -> SafetyResult:
    if not response or not response.strip():
        return SafetyResult(False, "Empty response")

    return SafetyResult(True)


def get_safe_fallback() -> str:
    return (
        "I can't help with harmful actions. "
        "I can help you think through the situation safely "
        "and find a constructive next step."
    )