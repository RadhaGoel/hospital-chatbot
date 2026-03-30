# FastAPI app for Hospital AI Assistant

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Import your vector DB
from backend.vector_store import loaded_vector_store

# Import local LLM (Ollama)
from langchain_ollama import OllamaLLM

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize LLM once (IMPORTANT: do not create inside function)
llm = OllamaLLM(model="llama3")


# Request body schema
class QueryRequest(BaseModel):
    query: str


# Root endpoint (just for testing)
@app.get("/")
def home():
    return {"message": "Hospital AI Assistant API is running"}


# Main chat endpoint
@app.post("/chat")
def chat(request: QueryRequest):
    user_query = request.query

    # Step 1: Retrieve similar chunks
    docs = loaded_vector_store.similarity_search(user_query)

    # Step 2: Extract context
    context = "\n".join([doc.page_content for doc in docs])

    # Step 3: Create prompt
    prompt = f"""
You are a helpful medical assistant.

Use ONLY the context below to answer the question.
Do not guess. If unsure, say you don't know.

Context:
{context}

Question:
{user_query}

Answer clearly and safely.
"""

    # Step 4: Get response from LLM
    response = llm.invoke(prompt)

    # Step 5: Return response
    return {
        "query": user_query,
        "response": response
    }