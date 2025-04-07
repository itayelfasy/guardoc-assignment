from backend.src.backend_config import CHROMA_DB_PATH
from backend.src.chroma_db_handler import ChromaDBHandler
from backend.src.models.patient_profile import PatientProfile

def generate_patients(num_records=1000):
    """
    Generate random patient records and insert them into the database.
    
    Args:
        num_records: Number of patient records to generate (default: 1000)
    """
    chroma_db_handler = ChromaDBHandler()
    documents = []
    metadatas = []
    ids = []

    print(f"Generating {num_records} random patient records...")
    for i in range(num_records):
        patient = PatientProfile.generate_random_patient()
        text = f"{patient.name} is {patient.age} years old. Diabetes: {patient.has_diabetes}. Hypertension: {patient.has_hypertension}. Smoker: {patient.smoker}. BMI: {patient.bmi}. Blood type: {patient.blood_type}. Allergies: {patient.has_allergies}. Takes medication: {patient.takes_medication}. Recent visit: {patient.recent_visit}."
        documents.append(text)
        metadatas.append(patient.model_dump(mode="json"))
        ids.append(str(i))
        
        # Print progress every 100 records
        if (i + 1) % 100 == 0:
            print(f"Generated {i + 1} records...")
    
    print("Inserting records into ChromaDB...")
    chroma_db_handler.add_documents(documents=documents, metadatas=metadatas, ids=ids)
    return f"✅ Successfully inserted {num_records} patient records into ChromaDB"

def main():
    """
    Main function to populate the database with random patient records.
    """
    print(f"Initializing ChromaDB at {CHROMA_DB_PATH}...")
    result = generate_patients()
    print(result)
    print("Database population complete!")

if __name__ == "__main__":
    main()