if any(word in text for word in [
    "angry", "mad", "furious", "annoyed",
    "irritated", "frustrated", "rage"
]):
    emotion = "angry"

elif any(word in text for word in [
    "sad", "upset", "hurt", "crying",
    "low", "down", "terrible", "miserable"
]):
    emotion = "sad"

elif any(word in text for word in [
    "worried", "anxious", "nervous",
    "scared", "overwhelmed", "stressed"
]):
    emotion = "anxious"

elif any(word in text for word in [
    "happy", "excited", "great",
    "good", "wonderful", "amazing"
]):
    emotion = "positive"
