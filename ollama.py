# ollama.py
import requests

OLLAMA_URL = "http://localhost:11411"

def ollama_generate(prompt, model="llama2"):
    url = f"{OLLAMA_URL}/generate"
    payload = {
        "model": model,
        "prompt": prompt,
    }
    response = requests.post(url, json=payload, stream=False)
    # If streaming = True, you'd read line by line, but let's keep it simple
    if response.status_code == 200:
        # The JSON from Ollama typically has:
        # {"done": false, "response": "..."} repeated lines if streaming
        # If not streaming, you get a single JSON with entire text
        result = response.json()
        # result["response"] should hold the generated text
        return result.get("response", "")
    else:
        raise Exception(f"Ollama API error: {response.text}")
