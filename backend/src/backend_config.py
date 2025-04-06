import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI Configuration
OPENAI_KEY = os.getenv('OPENAI_KEY')
CHAT_MODEL = os.getenv('CHAT_MODEL', 'gpt-3.5-turbo')  # Default model

# Database Configuration
CHROMA_DB_PATH = os.getenv('CHROMA_DB_PATH', './chroma_db')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'medical_documents')

# API Configuration
API_HOST = os.getenv('API_HOST', '0.0.0.0')
API_PORT = int(os.getenv('API_PORT', '8090'))
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'

# CORS Configuration
CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:3000').split(',')

# Optional configurations with defaults
MAX_TOKENS = int(os.getenv('MAX_TOKENS', '500'))
TEMPERATURE = float(os.getenv('TEMPERATURE', '0.7'))

# Validate required environment variables
if not OPENAI_KEY:
    raise ValueError("OPENAI_KEY environment variable is required")
