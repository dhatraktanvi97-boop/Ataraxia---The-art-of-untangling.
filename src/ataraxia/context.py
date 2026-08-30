from dataclasses import dataclass
from ataraxia.analyzer import analyze_message, AnalysisResult


@dataclass
class ConversationContext:
    user_message: str
    analysis: AnalysisResult
    recent_messages: list[str]


def create_context(
    user_message: str,
    recent_messages: list[str] | None = None
) -> ConversationContext:
    if recent_messages is None:
        recent_messages = []

    analysis = analyze_message(user_message)

    return ConversationContext(
        user_message=user_message.strip(),
        analysis=analysis,
        recent_messages=recent_messages
    )
