from embeddings import get_embeddings_model, embed_texts
from vector_store import create_chroma_db

def retrieve_relevant_chunks(query, k=3):
    model = get_embeddings_model()
    query_embedding = embed_texts([query], model)[0]

    collection = create_chroma_db()  # same DB name or path as used in build step
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )
    # 'results' is a dictionary with 'documents', etc.
    # Each 'documents' is a list of the top k chunk strings
    relevant_chunks = results["documents"][0]
    return relevant_chunks
