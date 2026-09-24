# RAG-Based Question Answering System
A Retrieval-Augmented Generation (RAG) application that answers questions using information retrieved from PDF documents.
The project uses **semantic search with ChromaDB** to retrieve relevant document chunks and **Groq LLM** to generate answers based on the retrieved context.

# Project Overview
The goal of this project is to build a complete RAG pipeline from scratch and understand how each component works.
The current pipeline is:
```text
PDF Documents
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Vector Embeddings
      ↓
ChromaDB
      ↓
Semantic Search
      ↓
Relevant Context
      ↓
Groq LLM
      ↓
Generated Answer
      ↓
FastAPI API
```
##  Features
* Load and extract text from multiple PDF documents
* Split documents into smaller chunks
* Generate vector embeddings using Sentence Transformers
* Store embeddings and document chunks in ChromaDB
* Perform semantic similarity search
* Retrieve the most relevant document chunks
* Generate answers using a Groq-hosted LLM
* Expose the RAG system through a FastAPI API

## Technologies Used

* **Python**
* **FastAPI** — API framework
* **Sentence Transformers** — text embeddings
* **ChromaDB** — vector database
* **LangChain Text Splitters** — document chunking
* **Groq** — LLM inference
* **OpenAI Python SDK** — OpenAI-compatible client for Groq

## 📁 Project Structure
```text
RAG/
│
├── app/
│   ├── main.py
│   ├── document_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── database.py
│   ├── retrieval.py
│   └── llm.py
│
├── data/
│   └── *.pdf
│
├── chromadb/
│   └── ChromaDB data
│
├── .env
├── .gitignore
└── README.md
```

### File Description

| File                 | Purpose                                          |
| -------------------- | ------------------------------------------------ |
| `main.py`            | FastAPI application and API endpoint             |
| `document_loader.py` | Loads and extracts text from PDFs                |
| `chunking.py`        | Splits documents into smaller chunks             |
| `embeddings.py`      | Converts text chunks into vector embeddings      |
| `database.py`        | Stores embeddings and documents in ChromaDB      |
| `retrieval.py`       | Performs semantic similarity search              |
| `llm.py`             | Sends retrieved context and questions to the LLM |

## Learning Goals

This project is being developed incrementally to understand the individual components of a RAG system rather than relying on a complete framework abstraction.

The main learning areas are:

* Document processing
* Chunking strategies
* Embeddings
* Vector databases
* Semantic retrieval
* LLM integration
* FastAPI
* RAG architecture
* Hybrid retrieval

## 📄 License

This project is for learning and experimentation.
