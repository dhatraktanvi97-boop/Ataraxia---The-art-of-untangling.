from dataclasses import dataclass


@dataclass
class SafetyResult:
    safe: bool
    reason: str = ""


def validate_response(response: str) -> SafetyResult:
    """
    Basic safety gate for AI-generated responses.

    This is a placeholder layer.
    A production system should use a dedicated safety classifier
    and additional policy checks.
    """

    if not response or not response.strip():
        return SafetyResult(False, "Empty response")

    return SafetyResult(True)


def get_safe_fallback() -> str:
    """Return a neutral fallback when a response fails safety checks."""
    return (
        "I can't help with harmful actions. "
        "I can help you think through the situation safely "
        "and find a constructive next step."
    )
