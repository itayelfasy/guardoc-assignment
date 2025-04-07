import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.src.backend_config import (
    API_HOST, API_PORT, DEBUG, CORS_ORIGINS
)
from backend.src.models.query import Query
from backend.src.services.question_service import QuestionService

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

# Initialize services
question_service = QuestionService()

@app.post("/ask_question")
async def ask_question(query: Query):
    """
    Process a question about medical documents and return an AI-generated answer.
    """
    return question_service.process_question(query.question)

if __name__ == '__main__':
    uvicorn.run(
        "app:app", 
        host=API_HOST, 
        port=API_PORT,
        reload=DEBUG
    )