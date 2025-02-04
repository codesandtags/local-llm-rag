from sentence_transformers import SentenceTransformer

def get_embeddings_model(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    return SentenceTransformer(model_name)

def embed_texts(texts, model):
    # model.encode returns a list of embeddings
    return model.encode(texts, convert_to_numpy=True)
