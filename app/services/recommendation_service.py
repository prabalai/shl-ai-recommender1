from retriever.chroma_store import (
    search_assessments
)

from services.ranking_service import (
    rank_results
)

def get_recommendations(query):

    retrieved = search_assessments(
        query=query,
        n_results=15
    )

    ranked = rank_results(
        retrieved,
        query
    )

    recommendations = []

    for item in ranked[:10]:

        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": item["keys"]
        })

    return recommendations