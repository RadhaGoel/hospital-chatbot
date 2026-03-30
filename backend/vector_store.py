import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from backend.split_data import chunks
# Create an instance of the HuggingFaceEmbeddings class
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create a FAISS vector store from the chunks and their embeddings
vector_store = FAISS.from_texts(chunks, embeddings)

# Save the vector store to disk
vector_store.save_local("faiss_vector_store")

# Load the vector store from disk
loaded_vector_store = FAISS.load_local(
    "faiss_vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)

# Example query
query = "high body temperature?"
# Perform a similarity search using the loaded vector store
similar_chunks = loaded_vector_store.similarity_search(query)

# Print the similar chunks
for i, chunk in enumerate(similar_chunks):
    print(f"Similar Chunk {i+1}:\n{chunk}\n")