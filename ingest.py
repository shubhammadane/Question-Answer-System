from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

PDF_FILE = "Soybean.pdf"

print("Loading PDF...")

loader = PyPDFLoader(PDF_FILE)
docs = loader.load()

print(f"Loaded {len(docs)} pages")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

print(f"Created {len(chunks)} chunks")

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

print("Creating Vector Database...")

db = FAISS.from_documents(
    chunks,
    embeddings
)

db.save_local("faiss_db")

print("FAISS Database Created Successfully!")