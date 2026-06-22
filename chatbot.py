from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

print("Loading Embeddings...")

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

print("Loading Vector Database...")

db = FAISS.load_local(
    "faiss_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k": 3})

print("Loading Llama3...")

llm = OllamaLLM(model="llama3")

print("\nChatbot Ready!")
print("Type 'exit' to quit\n")

while True:

    question = input("Question: ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a helpful document assistant.

Rules:
1. Answer ONLY from the provided context.
2. If answer is not available, say:
   "Information not found in document."
3. Answer in the SAME language as the user question.
4. Keep answers concise and clear.

Question:
{question}

Context:
{context}

Answer:
"""

    response = llm.invoke(prompt)

    print("\nAnswer:")
    print(response)
    print("\n" + "=" * 60 + "\n")