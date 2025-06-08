!pip install pymupdf faiss-cpu sentence-transformers
import fitz  # For reading PDF
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
doc = fitz.open(r"C:\Users\chand\Downloads\ipc_act.pdf")
text = "".join([page.get_text() for page in doc])
chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks, convert_to_numpy=True).astype("float32")
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
print(" IPC Chatbot ready! Type 'bye' to exit.")
while True:
    query = input("You: ")
    if query.lower() == "bye":
        print("Bot: Goodbye!")
        break
    query_vec = model.encode([query], convert_to_numpy=True).astype("float32")
    _, I = index.search(query_vec, 1)   
    answer = chunks[I[0][0]].strip()
    print("Bot:", answer if answer else "No info found.")
