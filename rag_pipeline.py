from retrieval import retrieve_relevant_chunks
from ollama import ollama_generate

def construct_prompt(chunks, user_query):
    context = "\n".join(chunks)
    prompt = f"""You are a helpful assistant. I have some context from a PDF:
---
{context}
---
Given this context and the following question, provide a concise answer.

Question: {user_query}
Answer:"""
    return prompt

def answer_query(user_query, model="llama2", k=3):
    # Retrieve top k relevant chunks
    relevant_chunks = retrieve_relevant_chunks(user_query, k=k)
    # Build prompt
    prompt = construct_prompt(relevant_chunks, user_query)
    # Call Ollama
    response = ollama_generate(prompt, model=model)
    return response
