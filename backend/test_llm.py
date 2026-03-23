# This file is for testing the LLM integration with Ollama.

#importing ollama model from langchain_community
from langchain_ollama import OllamaLLM

#loading the llama3 model from ollama
llama3model = OllamaLLM(model="llama3")

#sending a test prompt to the model and printing the response
response = llama3model.invoke("What is the cause  of malaria?")

#printing the response 
print(response)

