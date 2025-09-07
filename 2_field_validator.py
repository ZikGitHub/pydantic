from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com', 'sbi.com']

        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Invalid domain name")

        return value
    
    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator("age", mode="after")
    @classmethod
    def transform_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Invalid age")
        
    




def insert_patient_data(patient: Patient):
    print(patient)
    print("Data inserted!")


def update_patient_data(patient: Patient):
    print(patient)
    print("Data updated!")


patient_info = {
    "name": "John",
    "email": "john319@icici.com",
    "age": '70',
    "weight": 70.5,
    "married": True,
    "allergies": ["peanut", "milk"],
    "contact_details": {"phone": "123-456-7890"}
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)
