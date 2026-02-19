def health_type(text):
    t = text.lower()
    if any(w in t for w in [
        "tired", "stress", "angry", "confused",
        "depressed", "not able", "didn't", "forgot"
    ]):
        return "Unhealthy"
    return "Healthy"


def level_type(text):
    t = text.lower()

    if any(w in t for w in ["career", "future", "life", "study", "internship"]):
        return "Macro"

    if any(w in t for w in ["system", "tool", "workflow", "process", "zapier"]):
        return "Nano"

    return "Micro"
