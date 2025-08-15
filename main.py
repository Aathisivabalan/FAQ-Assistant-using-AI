from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import openai   # <- Ensure this import exists

openai.api_key = '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'

app = FastAPI()

model = SentenceTransformer('all-MiniLM-L6-v2')
documents = [
    "RAG stands for Retrieval-Augmented Generation. It enhances LLM responses by retrieving relevant data chunks before generation.",
    "FAISS is a library for efficient similarity search and clustering of dense vectors.",
    "LLMs are Large Language Models trained on massive text data to understand and generate human-like text."
]

embeddings = model.encode(documents)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
def ask_question(request: QueryRequest):
    query_embedding = model.encode([request.query])
    D, I = index.search(np.array(query_embedding), k=1)
    retrieved_doc = documents[I[0][0]]
    prompt = f"Answer based on context:\\nContext: {retrieved_doc}\\nQuestion: {request.query}"
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=100)
    return {"answer": response.choices[0].text.strip()}
