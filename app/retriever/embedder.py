import json
import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="shl_catalog"
)

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

with open(
    "app/catalog/assessments.json",
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)

for item in data:

    searchable_text = f"""
    Name: {item.get('name', '')}
    Description: {item.get('description', '')}
    Keys: {' '.join(item.get('keys', []))}
    """

    embedding = model.encode(
        searchable_text
    ).tolist()

    collection.add(
        ids=[str(item["entity_id"])],

        embeddings=[embedding],

        documents=[searchable_text],

        metadatas=[{
            "name": item["name"],
            "url": item["link"],
            "keys": ",".join(
                item.get("keys", [])
            )
        }]
    )

print("Embeddings created successfully!")