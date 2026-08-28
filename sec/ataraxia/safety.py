def safety_check(text):
    """
    Basic safety gate for Ataraxia responses.
    """

    harmful_topics = [
        "violence",
        "self-harm",
        "suicide",
        "harm someone"
    ]

    text_lower = text.lower()

    for topic in harmful_topics:
        if topic in text_lower:
            return False

    return True
