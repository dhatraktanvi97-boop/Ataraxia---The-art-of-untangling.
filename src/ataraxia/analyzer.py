from dataclasses import dataclass


@dataclass
class AnalysisResult:
    emotion: str
    intent: str
    situation: str


def analyze_message(message: str) -> AnalysisResult:
    """
    Basic rule-based message analysis.
    This is an initial prototype and will later be upgraded
    with proper NLP/ML models.
    """

    text = message.lower().strip()

    emotion = "neutral"
    intent = "unknown"

    # Emotion detection
    if any(word in text for word in [
        "angry", "mad", "furious", "annoyed", "irritated"
    ]):
        emotion = "angry"

    elif any(word in text for word in [
        "sad", "upset", "hurt", "crying", "low", "down"
    ]):
        emotion = "sad"

    elif any(word in text for word in [
        "worried", "anxious", "nervous", "scared"
    ]):
        emotion = "anxious"

    elif any(word in text for word in [
        "happy", "excited", "great", "good"
    ]):
        emotion = "positive"

    # Intent detection
    if any(word in text for word in [
        "argument", "argued", "fight", "conflict", "disagreement"
    ]):
        intent = "conflict"

    elif any(phrase in text for phrase in [
        "what should i do",
        "what can i do",
        "how should i",
        "need advice",
        "give me advice",
        "help me"
    ]):
        intent = "seeking_advice"

    elif any(phrase in text for phrase in [
        "i need to vent",
        "just need to vent",
        "let me vent",
        "i want to vent",
        "i just want to talk"
    ]):
        intent = "venting"

    return AnalysisResult(
        emotion=emotion,
        intent=intent,
        situation=message.strip()
    )
    
