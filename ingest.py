import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

PDF_FILE = "Soybean.pdf"
DB_FOLDER = "faiss_db"

print("Loading PDF...")

loader = PyPDFLoader(PDF_FILE)
documents = loader.load()

print(f"Loaded {len(documents)} pages")

print("Splitting document...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

print("Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3"
)

print("Creating FAISS vector database...")

vector_db = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)

print("Saving database...")

vector_db.save_local(DB_FOLDER)

print("===================================")
print("FAISS Database Created Successfully")
print(f"Saved in: {DB_FOLDER}")
print("===================================")