# Local Multilingual RAG Chatbot

## Overview

This project is a Local Retrieval-Augmented Generation (RAG) Chatbot that answers questions from uploaded documents.

The chatbot supports multiple Indian languages such as:

* English
* Hindi
* Marathi
* Tamil
* Telugu
* Gujarati
* Bengali
* Punjabi

The entire system runs locally on your machine without using any cloud APIs.

---

## Features

* Document-based Question Answering
* PDF Document Support
* Multilingual Query Support
* FAISS Vector Database
* Local Embedding Model
* Offline Processing
* Command Line Interface
* Easy to Extend with Streamlit UI

---

## Project Structure

```text
chatbot/
│
├── document.pdf
├── ingest.py
├── chatbot.py
├── faiss_db/
├── requirements.txt
└── README.md
```

---

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Required Packages

```bash
pip install langchain
pip install langchain-community
pip install sentence-transformers
pip install faiss-cpu
pip install pypdf
```

---

## Step 1: Load and Index Document

Run:

```bash
python ingest.py
```

This will:

1. Load the PDF
2. Split text into chunks
3. Generate embeddings
4. Store vectors in FAISS

---

## Step 2: Start Chatbot

Run:

```bash
python chatbot.py
```

Example:

```text
Question: What is GAN?

Answer:
GAN stands for Generative Adversarial Network...
```

---

## Multilingual Examples

### Marathi

```text
GAN म्हणजे काय?
```

### Hindi

```text
GAN क्या है?
```

### English

```text
What is GAN?
```

---

## Embedding Model

Recommended Model:

```text
BAAI/bge-m3
```

Advantages:

* Multilingual Support
* Fast Retrieval
* High Accuracy
* Works with Indian Languages

---

## Future Enhancements

* Streamlit Web UI
* Voice Input
* Chat History
* Multi-PDF Support
* Hybrid Search
* OCR Support
* Local LLM Integration using Ollama

---

## Technology Stack

* Python
* LangChain
* FAISS
* Sentence Transformers
* BGE-M3 Embeddings
* Ollama (Optional)
* Streamlit (Future)

---

## License

This project is for educational and research purposes.
