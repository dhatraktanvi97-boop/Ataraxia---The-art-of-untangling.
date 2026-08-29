from ataraxia.analyzer import AnalysisResult


def generate_response(analysis: AnalysisResult) -> str:
    """
    Generate a response based on detected emotion and intent.
    """

    # Conflict situations
    if analysis.intent == "conflict":
        if analysis.emotion == "angry":
            return (
                "You seem frustrated about the conflict. "
                "Before responding, give yourself some time to cool down. "
                "Then try to understand what caused the disagreement "
                "and discuss it calmly."
            )

        return (
            "It sounds like you're dealing with a conflict. "
            "Try to understand both sides of the situation "
            "and discuss the issue calmly rather than reacting immediately."
        )

    # Advice-seeking
    if analysis.intent == "seeking_advice":
        return (
            "Let's break the situation down into what happened, "
            "how you feel about it, and what outcome you want."
        )

    # Venting
    if analysis.intent == "venting":
        return (
            "It sounds like you need some space to express what you're feeling. "
            "You can explain what happened, and we'll work through it."
        )

    # Emotional states
    if analysis.emotion == "sad":
        return (
            "It sounds like you're having a difficult day. "
            "You don't have to figure everything out at once. "
            "If you want, tell me what has been making you feel this way."
        )

    if analysis.emotion == "anxious":
        return (
            "It sounds like something is making you feel worried or anxious. "
            "Let's take the situation one step at a time and identify "
            "what is within your control."
        )

    if analysis.emotion == "positive":
        return (
            "That sounds like a positive moment. "
            "What happened that made you feel this way?"
        )

    return (
        "Tell me a little more about what happened, "
        "and I'll help you understand the situation."
    )