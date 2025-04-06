import chromadb
from chromadb.config import Settings as ChromaSettings
from backend.src.backend_config import CHROMA_DB_PATH, COLLECTION_NAME


class ChromaDBHandler:
    def __init__(self):
        """Initialize the ChromaDB client with configuration from environment variables."""
        self.client = chromadb.Client(
            ChromaSettings(
                persist_directory=CHROMA_DB_PATH,
                is_persistent=True
            )
        )
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME
        )
    
    def query(self, query_text: str, n_results: int = 5):
        """
        Query the ChromaDB collection for relevant documents.
        
        Args:
            query_text: The text to search for
            n_results: Number of results to return
            
        Returns:
            Dictionary containing documents and their metadata
        """
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results
    
    def add_documents(self, documents: list[str], ids: list[str] = None):
        """
        Add documents to the ChromaDB collection.
        
        Args:
            documents: List of document texts
            ids: Optional list of document IDs
        """
        # if ids is None:
        #     ids = [f"doc_{i}" for i in range(len(documents))]
            
        self.collection.add(
            documents=documents,
            ids=ids
        )