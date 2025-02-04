# build_index.py
from pdf_reader import read_pdf
from embeddings import get_embeddings_model, embed_texts
from vector_store import create_chroma_db, add_texts_to_db
from chunk_text import chunk_text  # if you put chunk_text in a separate file

def build_vector_store_for_pdf(pdf_path):
    # Step 1: Read PDF
    pdf_text = read_pdf(pdf_path)

    # Step 2: Chunk text
    chunks = chunk_text(pdf_text, chunk_size=500, overlap=50)

    # Step 3: Embeddings
    model = get_embeddings_model()
    embeddings = embed_texts(chunks, model)

    # Step 4: Store in Chroma
    collection = create_chroma_db()
    add_texts_to_db(collection, chunks, embeddings)
    return collection
