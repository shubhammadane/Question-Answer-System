# 📚 Local Multilingual Document Question-Answer System

## Overview

This project is a local document-based Question Answering (QA) system built using Retrieval-Augmented Generation (RAG) concepts.

The system reads a PDF document, converts the content into vector embeddings, stores them in a FAISS vector database, and retrieves the most relevant information when a user asks a question.

Currently, the system performs semantic document retrieval. Future versions can integrate local Large Language Models (LLMs) such as Llama 3, Gemma, or Mistral through Ollama to generate natural-language answers.

---

## Features

* PDF Document Processing
* Semantic Search
* FAISS Vector Database
* Local Execution (No OpenAI API Required)
* Multilingual Query Support
* Fast Document Retrieval
* Extensible RAG Architecture
* Offline Processing

---

## Project Structure

```text
Question-Answer System/
│
├── Soybean.pdf
├── ingest.py
├── chatbot.py
├── faiss_db/
│   ├── index.faiss
│   └── index.pkl
│
└── README.md
```

---

## Technology Stack

* Python
* LangChain
* FAISS
* Hugging Face Embeddings
* Sentence Transformers
* PyPDF
* Ollama (Future Integration)

---

## Installation

### Clone Project

```bash
git clone <repository-url>
cd Question-Answer-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install langchain
pip install langchain-community
pip install langchain-text-splitters
pip install langchain-huggingface
pip install sentence-transformers
pip install faiss-cpu
pip install pypdf
```

---

## Step 1: Create Vector Database

Run:

```bash
python ingest.py
```

This process:

1. Loads the PDF document
2. Splits text into chunks
3. Creates embeddings
4. Builds a FAISS vector database
5. Saves the database locally

Expected Output:

```text
Loading PDF...
Loaded 44 pages
Splitting document...
Created 77 chunks
Creating FAISS vector database...
Saving database...
FAISS Database Created Successfully
```

---

## Step 2: Start Question Answering System

Run:

```bash
python chatbot.py
```

Expected Output:

```text
Chatbot Ready!
Type 'exit' to quit
```

---

## Example Questions

### English

```text
What is soybean?

What is the ideal soil pH for soybean?

What are the top management tips for soybean production?
```

### Marathi

```text
सोयाबीन म्हणजे काय?

सोयाबीनसाठी योग्य pH किती असावा?

सोयाबीन उत्पादनासाठी सर्वोत्तम व्यवस्थापन टिप्स कोणत्या आहेत?
```

### Hindi

```text
सोयाबीन क्या है?

सोयाबीन के लिए उपयुक्त pH कितना होना चाहिए?

सोयाबीन उत्पादन के लिए प्रमुख प्रबंधन सुझाव क्या हैं?
```

---

## Current Architecture

```text
PDF Document
      │
      ▼
Document Loader
      │
      ▼
Text Chunking
      │
      ▼
Embeddings
      │
      ▼
FAISS Vector Database
      │
      ▼
Retriever
      │
      ▼
Relevant Document Chunks
```

---

## Future Enhancements

* RAG Pipeline
* Ollama Integration
* Llama 3 Support
* Gemma Support
* Mistral Support
* Streamlit Web UI
* Voice Input
* Chat History
* Source Citations
* Multi-PDF Support
* Agricultural Advisory Chatbot

---

## Author

Developed as a learning project for Natural Language Processing (NLP), Information Retrieval, and Retrieval-Augmented Generation (RAG) systems.

---

## License

This project is intended for educational and research purposes.
