# load vector db
from vector_store import loaded_vector_store

# load local LLM (Ollama)
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

# take user query
user_query = input("Enter your medical query: ")

# retrieve relevant chunks
similar_chunks = loaded_vector_store.similarity_search(user_query)

# DEBUG (optional but good practice)
print("\n--- Retrieved Chunks ---")
for i, doc in enumerate(similar_chunks):
    print(f"\nChunk {i+1}:")
    print(doc.page_content)

# build context (IMPORTANT FIX)
context = "\n".join([doc.page_content for doc in similar_chunks])

# create prompt (IMPORTANT FIX)
prompt = f"""
You are a helpful medical assistant.

Use ONLY the context below to answer the question.

Context:
{context}

Question:
{user_query}

Answer clearly and safely.
"""

# send to LLM
response = llm.invoke(prompt)

# print final response
print("\n--- AI Response ---\n")
print(response)