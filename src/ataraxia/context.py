from dataclasses import dataclass


@dataclass
class ConversationContext:
    user_message: str
    emotion: str = "unknown"
    intent: str = "unknown"
    situation: str = "unknown"


def create_context(user_message: str) -> ConversationContext:
    """
    Create a basic context object from the user's message.
    Advanced NLP analysis will be added later.
    """

    return ConversationContext(
        user_message=user_message.strip()
    )