def recall_at_k(
    recommended,
    relevant,
    k=10
):

    recommended_k = recommended[:k]

    hits = len(
        set(recommended_k).intersection(
            set(relevant)
        )
    )

    return hits / len(relevant)