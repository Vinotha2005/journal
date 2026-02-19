def compute_metrics(text):
    t = text.lower()

    positivity = sum(t.count(w) for w in ["happy", "calm", "confident", "productive"]) * 10
    anger = sum(t.count(w) for w in ["angry", "irritated"]) * 10
    stress = sum(t.count(w) for w in ["stress", "tired", "exhausted"]) * 10
    improvement = sum(t.count(w) for w in ["learned", "improved", "fixed", "understood"]) * 10

    positivity = min(positivity + 40, 100)
    anger = min(anger + 20, 100)
    stress = min(stress + 30, 100)
    improvement = min(improvement + 40, 100)

    productivity = int((positivity + improvement - anger - stress) / 2)
    productivity = max(min(productivity, 100), 0)

    return {
        "positivity": positivity,
        "anger": anger,
        "stress": stress,
        "improvement": improvement,
        "productivity": productivity
    }
