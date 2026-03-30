#1. Load text from file
from backend.load_data import file_content

#2. import text splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

#3. create an instance of the text splitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)

#4. split the text into chunks
chunks = text_splitter.split_text(file_content)

#5. print the chunks
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")   
