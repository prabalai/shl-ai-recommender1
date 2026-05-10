def rerank_results(results, query):

    query = query.lower()

    scored = []

    for item in results:

        score = 0

        name = item["name"].lower()

        keys = item["keys"].lower()

        # TECHNICAL BOOSTS

        if "java" in query:

            if "java" in name:
                score += 15

            if "coding" in name:
                score += 10

        if "python" in query:

            if "python" in name:
                score += 15

        if "developer" in query \
        or "engineer" in query:

            if "knowledge" in keys:
                score += 10

            if "skills" in keys:
                score += 10

        # PERSONALITY BOOST

        if "personality" in query:

            if "personality" in keys:
                score += 5

        # MANAGEMENT BOOST

        if "manager" in query:

            if "personality" in keys:
                score += 6

        scored.append((score, item))

    scored.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [x[1] for x in scored]