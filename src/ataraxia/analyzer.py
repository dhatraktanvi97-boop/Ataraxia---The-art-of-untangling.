from dataclasses import dataclass


@dataclass
class AnalysisResult:
    emotion: str
    intent: str
    situation: str


def analyze_message(message: str) -> AnalysisResult:
    """
    Basic rule-based message analysis.
    This will later be replaced or enhanced with an NLP/ML model.
    """

    text = message.lower().strip()

    emotion = "neutral"
    intent = "unknown"

    if any(word in text for word in ["angry", "mad", "furious", "annoyed"]):
        emotion = "angry"
    elif any(word in text for word in ["sad", "upset", "hurt", "crying"]):
        emotion = "sad"
    elif any(word in text for word in ["worried", "anxious", "nervous"]):
        emotion = "anxious"
    elif any(word in text for word in ["happy", "excited", "great"]):
        emotion = "positive"

    if any(word in text for word in ["argument", "fight", "conflict", "argued"]):
        intent = "conflict"
    elif any(word in text for word in ["help", "advice", "what should", "how should"]):
        intent = "seeking_advice"
    elif any(word in text for word in ["feel", "feeling", "vent"]):
        intent = "venting"

    return AnalysisResult(
        emotion=emotion,
        intent=intent,
        situation=message.strip()
    )