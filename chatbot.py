from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

DB_FOLDER = "faiss_db"

print("Loading embeddings...")

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3"
)

print("Loading vector database...")

db = FAISS.load_local(
    DB_FOLDER,
    embeddings,
    allow_dangerous_deserialization=True
)

print("Chatbot Ready!")
print("Type 'exit' to quit")

while True:
    query = input("\nQuestion: ")

    if query.lower() == "exit":
        break

    docs = db.similarity_search(query, k=3)

    print("\nAnswer:\n")

    for i, doc in enumerate(docs, start=1):
        print(f"\n--- Result {i} ---")
        print(doc.page_content[:1000])