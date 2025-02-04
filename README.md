# Local PDF Q&A Chatbot with RAG + Ollama

This repository demonstrates how to build a local, Retrieval-Augmented Generation (RAG) system using open-source Python libraries, a local vector database (Chroma), and a locally running Large Language Model (LLM) via [Ollama](https://github.com/jmorganca/ollama).

The system:

1. **Reads and chunks a PDF** using Python.
2. **Embeds** those chunks and stores them in a **Chroma** vector database.
3. **Retrieves** the most relevant chunks for a user query.
4. **Sends** the query + relevant chunks to a **local LLM** (served by Ollama) to generate an answer.
5. **Provides** a **command-line chatbot** interface to ask questions about the PDF.

---

## Table of Contents

- [Local PDF Q\&A Chatbot with RAG + Ollama](#local-pdf-qa-chatbot-with-rag--ollama)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Architecture](#architecture)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Example](#example)
  - [How It Works](#how-it-works)
  - [Project structure](#project-structure)

---

## Features

- **Local Embeddings**: Uses a local embedding model (e.g., [sentence-transformers](https://github.com/UKPLab/sentence-transformers)) to embed the text.
- **Vector Database**: Stores embeddings in [Chroma](https://github.com/chroma-core/chroma) for fast similarity search.
- **Local LLM**: Relies on [Ollama](https://github.com/jmorganca/ollama) to serve a model like Llama 2 locally.
- **Secure & Private**: No external API calls—your PDF content stays on your machine.
- **Easy CLI**: Interactively ask questions about your PDF.

---

## Architecture

```
            ┌───────────┐
            │   PDF     │
            └────┬──────┘
                 │ Extract
                 ▼
        ┌────────────────────┐
        │    Chunk Text      │
        └────────────────────┘
                 │ Embedding
                 ▼
        ┌────────────────────┐
        │   Vector Store     │  (Chroma)
        └────────────────────┘
                 │ Query
                 ▼
User Query ───────> Embedding ────> Retrieve top K chunks
                │
                ▼
        ┌─────────────────────┐
        │ Construct Prompt    │
        └─────────────────────┘
                │
                ▼
        ┌─────────────────────┐
        │ Local LLM (Ollama)  │
        └─────────────────────┘
                │
                ▼
        Answer to User
```

## Installation

1. **Clone** this repository:

   ```bash
   git clone https://github.com/codesandtags/local-llm-rag.git
   cd local-llm-rag
   ```

2. Install Python dependencies. We recommend creating a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
# or "venv\Scripts\activate" on Windows

pip install -r requirements.txt
```

3. brew install ollama

```bash
brew install ollama
# Start Ollama
ollama serve
```

## Usage

1. Add your PDF to the project directory (or note its path).
2. Run the chatbot from the command line, specifying the PDF path:

```bash
python chat.py path/to/your.pdf
```

3. Interact with the chatbot:
   3.1 Type your question at the prompt.
   3.2 Type exit or quit to end the session.

### Example

```bash
$ python chat.py mydoc.pdf
Building the vector store...
Vector store built. You can now ask questions.

[User] > What is the summary of this document?
[Assistant] The document discusses...
```

## How It Works

1. PDF Reading

- We use pypdf to read each page’s text from the PDF, combining into a single string.

2. Chunking

- The combined text is split into overlapping chunks (e.g., 500 words with 50 words overlap).
- Overlapping helps preserve context between chunks.

3. Embedding & Storage

- Each chunk is embedded using sentence-transformers/all-MiniLM-L6-v2 (you can change the model if desired).
- The embeddings (vectors) are stored in a Chroma collection, along with the chunk text.

4. Retrieval

- When a user enters a query, we embed that query using the same embedding model, then run a similarity search against the chunk embeddings (in Chroma) to get the top K chunks (default k=3).

5. Prompt Construction

- We build a custom prompt that includes:
  - A brief system instruction: “You are a helpful assistant...”
  - The top K retrieved chunks as “context”
  - The user question 6. LLM Generation

The prompt is sent to the local Ollama instance via a POST request to http://localhost:11411/generate.
Ollama returns the model’s generated answer, which we print to the user.

## Project structure

```plaintext
local-llm-rag/
├── chat.py
├── build_index.py
├── pdf_reader.py
├── embeddings.py
├── vector_store.py
├── retrieval.py
├── rag_pipeline.py
├── ollama.py
├── requirements.txt
└── README.md
```
