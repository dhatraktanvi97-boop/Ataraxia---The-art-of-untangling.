from dataclasses import dataclass


@dataclass
class SafetyResult:
    safe: bool
    reason: str = ""


UNSAFE_PATTERNS = [
    "how to hurt",
    "how can i hurt",
    "how do i hurt",
    "i want to hurt",
    "i want to harm",
    "how to harm",
    "how can i harm",
    "how do i harm",
    "how to kill",
    "how can i kill",
    "how do i kill",
    "i want to kill",
    "i am going to kill",
    "i will kill",
    "i want him dead",
    "how to attack",
    "how can i attack",
    "how do i attack",
    "i want to attack",
    "how to poison",
    "how can i poison",
    "how do i poison",
    "how to make a weapon",
    "how to make a bomb",
]


def check_user_input(message: str) -> SafetyResult:
    if not message or not message.strip():
        return SafetyResult(False, "Empty user message")

    text = message.lower().strip()

    for pattern in UNSAFE_PATTERNS:
        if pattern in text:
            return SafetyResult(
                False,
                "Potentially harmful request or intent detected"
            )

    return SafetyResult(True)


def validate_response(response: str) -> SafetyResult:
    if not response or not response.strip():
        return SafetyResult(False, "Empty response")

    return SafetyResult(True)


def get_safe_fallback() -> str:
    return (
        "I can't help with harming someone. "
        "I can help you handle the situation safely "
        "and work toward a constructive next step."
    )