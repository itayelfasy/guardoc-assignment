# Medical Document Assistant

A full-stack application that provides a ChatGPT-style interface for asking questions about digital health documents. The system uses a vector database (ChromaDB) to store and retrieve relevant medical document information, and OpenAI's language models to generate accurate responses.

## Features

- **Modern React Frontend**: Clean, responsive UI built with React, TypeScript, and Material-UI
- **FastAPI Backend**: High-performance Python backend using FastAPI
- **Vector Database**: ChromaDB for efficient document storage and retrieval
- **AI-Powered Responses**: OpenAI integration for generating context-aware answers
- **Real-time Chat Interface**: Interactive chat experience similar to ChatGPT

## Project Structure

```
medical-document-assistant/
├── frontend/                 # React TypeScript frontend
│   ├── public/               # Static files
│   ├── src/                  # Source code
│   │   ├── components/       # React components
│   │   ├── services/         # API services
│   │   ├── App.tsx           # Main application component
│   │   └── index.tsx         # Application entry point
│   ├── package.json          # Frontend dependencies
│   └── tsconfig.json         # TypeScript configuration
│
├── backend/                  # Python FastAPI backend
│   ├── src/                  # Source code
│   │   ├── models/           # Data models
│   │   ├── app.py            # Main FastAPI application
│   │   ├── chroma_db_handler.py  # ChromaDB integration
│   │   ├── backend_config.py # Configuration settings
│   │   └── populate_db.py    # Script to populate the database
│   ├── chroma_db/            # Vector database storage
│   └── .env                  # Environment variables
│
└── README.md                 # Project documentation
```

## Prerequisites

- Node.js (v14 or higher)
- Python (v3.8 or higher)
- OpenAI API key

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your environment variables:

   - Create a `.env` file in the backend directory
   - Add the following environment variables:

   ```
   # Required
   OPENAI_KEY=your_api_key_here

   # OpenAI Configuration
   CHAT_MODEL=gpt-3.5-turbo
   MAX_TOKENS=500
   TEMPERATURE=0.7

   # Database Configuration
   CHROMA_DB_PATH=chroma_db
   COLLECTION_NAME=medical_documents

   # API Configuration
   API_HOST=0.0.0.0
   API_PORT=8080
   DEBUG=false

   # CORS Configuration
   CORS_ORIGINS=http://localhost:3000
   ```

5. Populate the database with medical documents:

   ```bash
   python src/populate_db.py
   ```

6. Start the backend server:
   ```bash
   python src/app.py
   ```
   The server will run on http://localhost:8080

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```
   The application will open in your browser at http://localhost:3000

## Environment Variables

### Backend (.env)

| Variable        | Description                             | Default               |
| --------------- | --------------------------------------- | --------------------- |
| OPENAI_KEY      | Your OpenAI API key                     | (Required)            |
| CHAT_MODEL      | OpenAI model to use                     | gpt-3.5-turbo         |
| MAX_TOKENS      | Maximum tokens for OpenAI response      | 500                   |
| TEMPERATURE     | Temperature for OpenAI response (0-1)   | 0.7                   |
| CHROMA_DB_PATH  | Path to ChromaDB storage                | chroma_db             |
| COLLECTION_NAME | Name of the ChromaDB collection         | medical_documents     |
| API_HOST        | Host to run the API server              | 0.0.0.0               |
| API_PORT        | Port to run the API server              | 8080                  |
| DEBUG           | Enable debug mode                       | false                 |
| CORS_ORIGINS    | Comma-separated list of allowed origins | http://localhost:3000 |

## Usage

1. Open the application in your web browser
2. Type your medical document-related question in the input field
3. Press Enter or click the Send button
4. The system will retrieve relevant information from the database and generate a response
5. The response will appear in the chat interface

## API Endpoints

### POST /ask_question

Sends a question to the backend and receives an AI-generated response based on the medical documents in the database.

**Request Body:**

```json
{
  "question": "What are the symptoms of diabetes?"
}
```

**Response:**

```json
{
  "answer": "Based on the medical documents, the symptoms of diabetes include..."
}
```

## Technologies Used

- **Frontend**: React, TypeScript, Material-UI
- **Backend**: FastAPI, Python
- **Database**: ChromaDB (vector database)
- **AI**: OpenAI API
- **Styling**: Emotion, Material-UI theming

## Development

### Adding New Features

1. **Adding New Document Types**:

   - Update the `PatientProfile` model in `backend/src/models/patient_profile.py`
   - Modify the `populate_db.py` script to include new document types

2. **Customizing the UI**:

   - Modify components in `frontend/src/components/`
   - Update the theme in `frontend/src/App.tsx`

3. **Extending the API**:
   - Add new endpoints in `backend/src/app.py`
   - Create new models in `backend/src/models/`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributors

- [Your Name]

## Acknowledgments

- OpenAI for providing the language models
- ChromaDB team for the vector database
- FastAPI and React communities for the excellent frameworks
