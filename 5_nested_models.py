from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    gender: str = 'male'
    age: int
    address: Address


address_dict = {'city':'Gurgaon', 'state':'Haryana', 'pin':'122001'}
address1 = Address(**address_dict)

patient_dict = {'name':'nitish','age':35, 'address': address1}
patient1 = Patient(**patient_dict)
print(patient1)
print(patient1.address.city)


temp = patient1.model_dump_json(exclude_unset=True)

print(temp)
print(type(temp))