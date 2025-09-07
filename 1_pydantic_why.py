from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated



class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patientin less than 50 chars', examples=['nitish', 'john'])]
    email: EmailStr
    linkedIn: Optional[AnyUrl] = None
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not?')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Optional[Dict[str, str]] = {}



def insert_patient_data(patient: Patient):
    print(patient)
    print('Data inserted!')


def update_patient_data(patient: Patient):
    print(patient)
    print('Data updated!')


patient_info = {
    "name": "John", 
    "email": "john319@gmail.com",
    "linkedIn": "https://www.linkedin.com/in/john/",
    "age": 30, 
    'weight': 70.5, 
    'married': True, 
    'contact_details': {'phone': '123-456-7890'}
    }
                
patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)

