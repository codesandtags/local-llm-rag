import requests
import os
import json

OLLAMA_URL = "http://localhost:11434"  # or your updated host/port
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama2-uncensored")

def ollama_generate(prompt, model=None):
    if model is None:
        model = OLLAMA_MODEL

    url = f"{OLLAMA_URL}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True  # or just omit if Ollama streams by default
    }

    print(f"🤖 Sending prompt to Ollama: {prompt}")

    # Note stream=True here so we can read lines as they arrive
    response = requests.post(url, json=payload, stream=True)

    if response.status_code != 200:
        raise Exception(f"Ollama API error: {response.text}")

    # We'll collect all partial responses into one final answer
    text_parts = []

    # Read line by line
    for line in response.iter_lines(decode_unicode=True):
        if not line:
            continue  # skip empty lines

        # Each line should be valid JSON (like {"response": "...", "done": false/true})
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            # Ollama might send some lines that are not JSON.
            # If that's the case, you may need to handle or skip them.
            continue

        # Extract partial text from "response"
        chunk = data.get("response", "")
        text_parts.append(chunk)

        # If "done": True, we can stop reading
        if data.get("done", False):
            break

    # Join all partial responses into one final string
    full_answer = "".join(text_parts)
    return full_answer
