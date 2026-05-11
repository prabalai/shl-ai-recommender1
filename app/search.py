import json

with open(
    "app/catalog/assessments.json",
    "r",
    encoding="utf-8"
) as f:

    DATASET = json.load(f)

def search_assessments(query):

    query = query.lower()

    results = []

    for item in DATASET:

        searchable = (
            item.get("name", "") + " " +
            item.get("description", "") + " " +
            " ".join(item.get("keys", []))
        ).lower()

        score = 0

        for word in query.split():

            if word in searchable:
                score += 1

        results.append((score, item))

    results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [x[1] for x in results[:10]]
