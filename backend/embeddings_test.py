from sentence_transformers import SentenceTransformer

#Load the pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2') 

#take chunks from split_data.py
from split_data import chunks
#Generate embeddings for each chunk
embeddings = model.encode(chunks)
#Print the embeddings
for i, embedding in enumerate(embeddings):
    print(f"Embedding for Chunk {i+1}:\n{embedding}\n")     

    