from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


class NLPClassifier:
    def __init__(self):
        self.emotion_vectorizer = TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2)
        )

        self.intent_vectorizer = TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2)
        )

        self.emotion_model = LogisticRegression(max_iter=1000)
        self.intent_model = LogisticRegression(max_iter=1000)

        self._train()

    def _train(self):
        emotion_texts = [
            "I am angry",
            "I am furious",
            "I am really pissed off",
            "I am frustrated",
            "I feel sad",
            "I am feeling low",
            "I feel unhappy",
            "I am upset",
            "I am worried",
            "I feel anxious",
            "I am nervous",
            "I am scared",
            "I am happy",
            "I feel great",
            "I am excited",
            "Today is wonderful",
            "I am okay",
            "Everything is normal",
            "I feel fine",
        ]

        emotion_labels = [
            "angry", "angry", "angry", "angry",
            "sad", "sad", "sad", "sad",
            "anxious", "anxious", "anxious", "anxious",
            "positive", "positive", "positive", "positive",
            "neutral", "neutral", "neutral",
        ]

        intent_texts = [
            "I had an argument with my brother",
            "We had a fight",
            "I am having a conflict with my friend",
            "My brother and I disagreed",
            "What should I do?",
            "Can you give me some advice?",
            "What can I do about this?",
            "How should I handle this?",
            "I just want to talk",
            "I need to vent",
            "I want to express how I feel",
            "I need someone to listen",
            "I am telling you what happened",
            "Something happened today",
            "I want to share something",
        ]

        intent_labels = [
            "conflict", "conflict", "conflict", "conflict",
            "seeking_advice", "seeking_advice",
            "seeking_advice", "seeking_advice",
            "venting", "venting", "venting", "venting",
            "unknown", "unknown", "unknown",
        ]

        emotion_features = self.emotion_vectorizer.fit_transform(
            emotion_texts
        )

        intent_features = self.intent_vectorizer.fit_transform(
            intent_texts
        )

        self.emotion_model.fit(
            emotion_features,
            emotion_labels
        )

        self.intent_model.fit(
            intent_features,
            intent_labels
        )

    def predict_emotion(self, message: str) -> str:
        features = self.emotion_vectorizer.transform([message])
        return self.emotion_model.predict(features)[0]

    def predict_intent(self, message: str) -> str:
        features = self.intent_vectorizer.transform([message])
        return self.intent_model.predict(features)[0]


nlp_classifier = NLPClassifier()
