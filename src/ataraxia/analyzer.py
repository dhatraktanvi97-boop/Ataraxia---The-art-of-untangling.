from dataclasses import dataclass
from ataraxia.nlp import nlp_classifier


@dataclass
class AnalysisResult:
    emotion: str
    intent: str
    situation: str


def analyze_message(message: str) -> AnalysisResult:
    """
    Analyze a message using the NLP classifier.
    """

    text = message.lower().strip()

    emotion = nlp_classifier.predict_emotion(text)
    intent = nlp_classifier.predict_intent(text)

    return AnalysisResult(
        emotion=emotion,
        intent=intent,
        situation=message.strip(),
    )