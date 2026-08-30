from dataclasses import dataclass


@dataclass
class SafetyResult:
    safe: bool
    reason: str = ""


UNSAFE_PATTERNS = [
    "how to hurt",
    "how can i hurt",
    "how do i hurt",
    "how to harm",
    "how can i harm",
    "how do i harm",
    "how to kill",
    "how can i kill",
    "how do i kill",
    "how to attack",
    "how can i attack",
    "how do i attack",
    "how to poison",
    "how can i poison",
    "how do i poison",
    "how to make a weapon",
    "how to make a bomb",
    "hurt my brother",
    "hurt my sister",
    "kill my brother",
    "kill my sister",
    "attack my brother",
    "attack my sister",
]


def check_user_input(message: str) -> SafetyResult:
    if not message or not message.strip():
        return SafetyResult(False, "Empty user message")

    text = message.lower().strip()

    for pattern in UNSAFE_PATTERNS:
        if pattern in text:
            return SafetyResult(
                False,
                "Potentially harmful request detected"
            )

    return SafetyResult(True)


def validate_response(response: str) -> SafetyResult:
    if not response or not response.strip():
        return SafetyResult(False, "Empty response")

    return SafetyResult(True)


def get_safe_fallback() -> str:
    return (
        "I can't help with harming someone. "
        "I can help you handle the conflict safely "
        "and work out a constructive next step."
    )