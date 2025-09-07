from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict


class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)


def insert_patient_data(patient: Patient):
    print(patient)
    print("Data inserted!")


def update_patient_data(patient: Patient):
    print(patient)
    print("Data updated!")


patient_info = {
    "name": "John",
    "email": "john319@icici.com",
    "age": "70",
    "weight": 70.5,
    "height": 1.75,
    "married": True,
    "allergies": ["peanut", "milk"],
    "contact_details": {"phone": "123-456-7890"},
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)
