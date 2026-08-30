from ataraxia.context import ConversationContext


def generate_response(context: ConversationContext) -> str:
    """
    Generate a response using the current analysis and recent conversation.
    """

    emotion = context.analysis.emotion
    intent = context.analysis.intent
    recent_messages = context.recent_messages

    # Use previous conversation when available
    has_previous_context = len(recent_messages) > 0

    # Conflict + anger
    if intent == "conflict" and emotion == "angry":
        return (
            "It sounds like the conflict has left you frustrated. "
            "Before continuing the conversation, take a moment to pause. "
            "Then focus on what actually caused the disagreement "
            "and try to discuss it calmly."
        )

    # Conflict + sadness
    if intent == "conflict" and emotion == "sad":
        return (
            "It sounds like the conflict has affected you emotionally. "
            "Give yourself some time to process what happened. "
            "When you're ready, try to understand both sides "
            "before deciding how to respond."
        )

    # Conflict + anxiety
    if intent == "conflict" and emotion == "anxious":
        return (
            "It sounds like the conflict is making you feel worried. "
            "Try to separate what actually happened from what you're "
            "afraid might happen next. Focus on what you can control."
        )

    # Conflict
    if intent == "conflict":
        return (
            "It sounds like you're dealing with a conflict. "
            "Try to understand both sides of the situation "
            "and discuss the issue calmly rather than reacting immediately."
        )

    # Advice-seeking with previous context
    if intent == "seeking_advice" and has_previous_context:
        return (
            "Based on what you've shared so far, let's look at the situation "
            "step by step and focus on what you can do next."
        )

    # Advice-seeking
    if intent == "seeking_advice":
        return (
            "Let's break the situation down into three parts: "
            "what happened, how you feel about it, and what outcome "
            "you want. That will make the next step clearer."
        )

    # Venting
    if intent == "venting":
        return (
            "It sounds like you need some space to express what you're feeling. "
            "You can explain what happened, and we'll work through it."
        )

    # Emotional states
    if emotion == "angry":
        return (
            "You sound frustrated right now. "
            "Before reacting, take a moment to pause and identify "
            "what specifically triggered that feeling."
        )

    if emotion == "sad":
        return (
            "It sounds like you're having a difficult day. "
            "You don't have to figure everything out at once. "
            "If you want, tell me what has been making you feel this way."
        )

    if emotion == "anxious":
        return (
            "It sounds like something is making you feel worried or anxious. "
            "Let's take the situation one step at a time and identify "
            "what is within your control."
        )

    if emotion == "positive":
        return (
            "That sounds like a positive moment. "
            "What happened that made you feel this way?"
        )

    # Previous context but unknown emotion/intent
    if has_previous_context:
        return (
            "I have some context from what you shared earlier. "
            "Tell me a little more about what you're experiencing now."
        )

    return (
        "Tell me a little more about what happened, "
        "and I'll help you understand the situation."
    )
    
