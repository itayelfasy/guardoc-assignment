import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai
from backend.src.backend_config import (
    OPENAI_KEY, CHAT_MODEL, API_HOST, API_PORT, DEBUG,
    CORS_ORIGINS, MAX_TOKENS, TEMPERATURE
)
from backend.src.chroma_db_handler import ChromaDBHandler
from backend.src.models.query import Query

# Configure OpenAI
openai.api_key = OPENAI_KEY

# Initialize FastAPI app
app = FastAPI(
    title="Medical Document Assistant API",
    description="API for querying medical documents using AI",
    version="1.0.0",
    debug=DEBUG
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type", "Accept"],
    expose_headers=["Content-Type"],
    max_age=3600,
)

@app.post("/ask_question")
async def ask_question(query: Query):
    """
    Process a question about medical documents and return an AI-generated answer.
    """
    chroma_db_handler = ChromaDBHandler()
    results = chroma_db_handler.query(query_text=query.question)
    context = "/n".join(results["documents"][0])
    
    try:
        response = openai.ChatCompletion.create(
            model=CHAT_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant with access to medical data records."},
                {"role": "user",
                 "content": f"Answer the question using the following data:\n{context}\n\nQuestion: {query.question}"}
            ],
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        )
        return {"answer": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    uvicorn.run(
        "app:app", 
        host=API_HOST, 
        port=API_PORT,
        reload=DEBUG
    )