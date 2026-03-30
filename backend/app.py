# FastAPI app for Hospital AI Assistant

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.db_query import get_all_doctors, get_doctors_by_specialization

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
    user_query = request.query.lower()

    #STEP 1: DATABASE LOGIC
    if "doctor" in user_query:

        if "heart" in user_query:
            doctors = get_doctors_by_specialization("Cardio")

        elif "skin" in user_query:
            doctors = get_doctors_by_specialization("Derma")

        elif "brain" in user_query:
            doctors = get_doctors_by_specialization("Neuro")

        else:
            doctors = get_all_doctors()

        if doctors:
            formatted = "\n".join([f"{d[0]} - {d[1] if len(d)>1 else ''}" for d in doctors])

            return {
                "query": request.query,
                "response": f"Here are available doctors:\n{formatted}"
            }

        else:
            return {
                "response": "No doctors found."
            }

    #STEP 2: RAG LOGIC (existing)
    docs = loaded_vector_store.similarity_search(request.query)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a helpful medical assistant.

Give:
- possible causes
- precautions
- when to see a doctor

Context:
{context}

Question:
{request.query}
"""

    response = llm.invoke(prompt)

    return {
        "query": request.query,
        "response": response
    }