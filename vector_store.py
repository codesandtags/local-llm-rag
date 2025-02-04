import chromadb

def create_chroma_db(persist_directory="db_chroma"):
    """
    Creates or retrieves a persistent Chroma collection named 'pdf_chunks',
    stored in the specified persist_directory.
    """
    # Initialize a persistent client; data is stored in `persist_directory`
    client = chromadb.PersistentClient(path=persist_directory)

    # Create or get the collection for our PDF chunks
    collection = client.get_or_create_collection("pdf_chunks")
    return collection

def add_texts_to_db(collection, texts, embeddings):
    """
    Adds a list of text chunks and their corresponding embeddings to the
    provided Chroma collection. Assigns unique IDs and optional metadata.
    """
    # Generate unique IDs for each chunk
    ids = [f"chunk_{i}" for i in range(len(texts))]

    # Create metadata, for example storing the chunk index
    metadatas = [{"chunk_index": i} for i in range(len(texts))]

    # Add documents, embeddings, and metadata to the collection
    collection.add(
        documents=texts,       # the raw text of the chunks
        metadatas=metadatas,   # any metadata
        ids=ids,               # unique IDs for each chunk
        embeddings=embeddings  # vector embeddings (must match the order of texts)
    )
