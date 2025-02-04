import chromadb
from chromadb.config import Settings

def create_chroma_db(persist_directory="db_chroma"):
    client = chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory=persist_directory
    ))
    collection = client.get_or_create_collection("pdf_chunks")
    return collection

def add_texts_to_db(collection, texts, embeddings):
    # Each chunk needs a unique ID
    ids = [f"chunk_{i}" for i in range(len(texts))]
    metadatas = [{"chunk_index": i} for i in range(len(texts))]

    collection.add(
        documents=texts,
        metadatas=metadatas,
        ids=ids,
        embeddings=embeddings
    )
