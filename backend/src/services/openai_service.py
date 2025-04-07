import openai
from backend.src.backend_config import (
    OPENAI_KEY, CHAT_MODEL, MAX_TOKENS, TEMPERATURE
)

class OpenAIService:
    """Service for handling OpenAI API interactions."""
    
    def __init__(self):
        """Initialize the OpenAI service with API key from config."""
        openai.api_key = OPENAI_KEY

    def generate_response(self,context: str, question: str) -> str:
        """
        Generate a response using OpenAI's API based on the provided context and question.

        Args:
            context: The context information retrieved from the database
            question: The user's question

        Returns:
            The generated response text

        Raises:
            Exception: If there's an error with the OpenAI API call
        """
        try:
            response = openai.ChatCompletion.create(
                model=CHAT_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a medical document assistant that helps answer questions about patient records and medical conditions. "
                                 "Provide accurate, concise answers based only on the information provided in the context. "
                                 "If the information isn't in the context, say 'I don't have enough information to answer that question.'"
                    },
                    {
                        "role": "user",
                        "content": f"Answer the question using the following data:\n{context}\n\nQuestion: {question}"
                    }
                ],
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error generating response from OpenAI: {str(e)}")