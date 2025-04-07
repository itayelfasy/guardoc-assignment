from backend.src.chroma_db_handler import ChromaDBHandler
from backend.src.services.openai_service import OpenAIService

class QuestionService:
    """Service for processing questions and generating answers."""
    
    def __init__(self):
        """Initialize the question service with required handlers."""
        self.chroma_db_handler = ChromaDBHandler()
        self.openai_service = OpenAIService()
    
    def process_question(self, question: str) -> dict:
        """
        Process a question by retrieving relevant context and generating an answer.
        
        Args:
            question: The user's question
            
        Returns:
            Dictionary containing the answer or error message
            
        Raises:
            Exception: If there's an error processing the question
        """
        try:
            results = self.chroma_db_handler.query(query_text=question)

            if not results["documents"][0]:
                return {"answer": "I couldn't find any relevant information to answer your question."}
                
            context = "\n".join(results["documents"][0])

            answer = self.openai_service.generate_response(context, question)
            
            return {"answer": answer}
            
        except Exception as e:
            return {"error": str(e)} 