from ataraxia.analyzer import AnalysisResult


def generate_response(analysis: AnalysisResult) -> str:
    """
    Generate a basic response based on the detected emotion and intent.
    """

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

    if analysis.intent == "seeking_advice":
        return (
            "Let's break the situation down into what happened, "
            "how you feel about it, and what outcome you want."
        )

    if analysis.intent == "venting":
        return (
            "It sounds like you need some space to express what you're feeling. "
            "You can explain what happened, and we'll work through it."
        )

    return (
        "Tell me a little more about what happened, "
        "and I'll help you understand the situation."
    )