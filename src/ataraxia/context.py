from dataclasses import dataclass
from ataraxia.analyzer import analyze_message, AnalysisResult


@dataclass
class ConversationContext:
    user_message: str
    analysis: AnalysisResult


def create_context(user_message: str) -> ConversationContext:
    analysis = analyze_message(user_message)

    return ConversationContext(
        user_message=user_message.strip(),
        analysis=analysis
    )