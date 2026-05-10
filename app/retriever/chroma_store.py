import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="shl_catalog"
)

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def search_assessments(
    query: str,
    n_results: int = 10
):

    embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results
    )

    return results["metadatas"][0]