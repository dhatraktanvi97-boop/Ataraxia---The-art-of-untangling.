from dataclasses import dataclass


@dataclass
class AnalysisResult:
    emotion: str
    intent: str
    situation: str


def detect_emotion(text: str) -> str:
    """
    Detect the dominant emotional state from the user's message.
    This is currently rule-based and will later be upgraded
    with an NLP/ML model.
    """

    angry_patterns = [
        "angry",
        "mad",
        "furious",
        "annoyed",
        "irritated",
        "frustrated",
        "pissed off",
        "fed up",
        "rage",
    ]

    sad_patterns = [
        "sad",
        "upset",
        "hurt",
        "crying",
        "low",
        "feeling low",
        "down",
        "terrible",
        "miserable",
        "lonely",
        "hopeless",
    ]

    anxious_patterns = [
        "worried",
        "anxious",
        "nervous",
        "scared",
        "overwhelmed",
        "stressed",
        "stress",
        "panicking",
        "panic",
    ]

    positive_patterns = [
        "happy",
        "excited",
        "great",
        "good",
        "wonderful",
        "amazing",
        "glad",
        "proud",
        "relieved",
    ]

    if any(pattern in text for pattern in angry_patterns):
        return "angry"

    if any(pattern in text for pattern in sad_patterns):
        return "sad"

    if any(pattern in text for pattern in anxious_patterns):
        return "anxious"

    if any(pattern in text for pattern in positive_patterns):
        return "positive"

    return "neutral"


def detect_intent(text: str) -> str:
    """
    Detect what the user is trying to communicate or achieve.
    """

    conflict_patterns = [
        "argument",
        "argued",
        "fight",
        "fighting",
        "conflict",
        "disagreement",
        "dispute",
        "we fought",
        "had a fight",
    ]

    advice_patterns = [
        "what should i do",
        "what can i do",
        "how should i",
        "what do i do",
        "need advice",
        "give me advice",
        "help me",
        "can you help",
        "i don't know what to do",
    ]

    venting_patterns = [
        "i need to vent",
        "just need to vent",
        "let me vent",
        "i want to vent",
        "i just want to talk",
        "i need someone to listen",
        "just listen",
    ]

    if any(pattern in text for pattern in conflict_patterns):
        return "conflict"

    if any(pattern in text for pattern in advice_patterns):
        return "seeking_advice"

    if any(pattern in text for pattern in venting_patterns):
        return "venting"

    return "unknown"


def analyze_message(message: str) -> AnalysisResult:
    """
    Analyze the user's message and return structured information.
    """

    text = message.lower().strip()

    emotion = detect_emotion(text)
    intent = detect_intent(text)

    return AnalysisResult(
        emotion=emotion,
        intent=intent,
        situation=message.strip(),
    )