import pandas as pd

DATA_PATH = "data/journals.csv"

def search_journals(query):
    if not query.strip():
        return []

    keywords = [w.lower() for w in query.split() if len(w) > 3]

    try:
        df = pd.read_csv(DATA_PATH)
    except:
        return []

    results = []

    for _, row in df.iterrows():
        sentences = row["journal"].split(".")
        matches = []

        for s in sentences:
            if any(k in s.lower() for k in keywords):
                matches.append(s.strip())

        if matches:
            results.append({
                "date": row["date"],
                "matches": matches,
                "full": row["journal"]
            })

    return results
