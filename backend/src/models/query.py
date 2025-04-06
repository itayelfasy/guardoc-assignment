from pydantic import BaseModel, Field

class Query(BaseModel):
    """
    Pydantic model for the query request.
    """
    question: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="The question to ask about medical documents"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "question": "What are the symptoms of diabetes?"
            }
        } 