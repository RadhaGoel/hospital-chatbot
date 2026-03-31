# Hospital AI Assistant

An AI-powered medical chatbot built using LLMs, RAG, and a hybrid data system.

## Features

- 💬 ChatGPT-style UI
- 🧠 RAG (Retrieval Augmented Generation)
- 🔍 FAISS vector database for medical knowledge
- 🏥 SQLite database for hospital data (doctors)
- ⚡ FastAPI backend
- 🤖 Local LLM using Ollama (Llama3)

## Architecture

User Query → FastAPI →  
→ RAG (FAISS) OR Database (SQLite) →  
→ LLM (Ollama) → Response

## Tech Stack

- Python
- FastAPI
- LangChain
- FAISS
- SQLite
- HTML/CSS/JS
- Ollama (Llama3)

## Example Queries

- "I have fever and headache"
- "Show doctors"
- "Doctor for heart problem"

## Future Work

- Appointment booking system
- Chat memory
- PDF medical report analysis
- Deployment

---