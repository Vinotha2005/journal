def painway_type(text):
    t = text.lower()

    if any(w in t for w in ["didn't", "not able", "forgot", "stuck"]):
        return "Existing Unhealthy Painway"

    if any(w in t for w in ["fear", "worried", "might"]):
        return "Possible Unhealthy Painway"

    if any(w in t for w in ["completed", "did", "attended", "finished"]):
        return "Existing Healthy Pathway"

    if any(w in t for w in ["want to", "need to", "plan", "will"]):
        return "Possible Healthy Pathway"

    return "Existing Healthy Pathway"
