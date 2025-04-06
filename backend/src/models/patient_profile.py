from pydantic import BaseModel
from typing import Literal
import random
from faker import Faker

fake = Faker()
class PatientProfile(BaseModel):
    name: str
    age: int
    has_diabetes: bool
    has_hypertension: bool
    smoker: bool
    bmi: float
    blood_type: Literal["A", "B", "AB", "O"]
    has_allergies: bool
    takes_medication: bool
    recent_visit: str

    @classmethod
    def generate_random_patient(cls):
        return cls(
            name=fake.name(),
            age=random.randint(20, 90),
            has_diabetes=random.choice([True, False]),
            has_hypertension=random.choice([True, False]),
            smoker=random.choice([True, False]),
            bmi=round(random.uniform(18.0, 35.0), 1),
            blood_type=random.choice(["A", "B", "AB", "O"]),
            has_allergies=random.choice([True, False]),
            takes_medication=random.choice([True, False]),
            recent_visit=fake.date_this_year().isoformat()
        )


