from pydantic import BaseModel, EmailStr, Field, field_validator , model_validator
from typing import List, Dict, Optional, Annotated


class Student(BaseModel):
    
    #name: str = Field(max_length=50)
    name: str
    age: int 
    roll: float 
    email: EmailStr 
    married: bool
    leaves: List[int]
    subjects: Dict[str, int] 
    
    #fiel validator only validates 1 data variable
    #model validator takes more than 1 field data
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 20 and model.married is False:
            raise ValueError(f"{model.name} is a unmarried major!! with marital status {model.married}")
        
        return model
    
    
    
    @field_validator('email')
    @classmethod
    
    def email_validator(cls, value):
        valid_domains = ['yahoo.com','hdfc.com','gmail.com']
        vals = value.split(sep='@')[-1]
        if vals not in valid_domains:
            raise ValueError("Not an ideal domain")
        
        return value
            
    @field_validator('name')
    @classmethod
    def validate_name(cls, n1):
        if len(n1) > 50:
            raise ValueError("Given name exceeds 50 character length")
        return n1
    
    @field_validator('leaves')
    @classmethod
    def validating_leaves(cls, l):
        for i in l:
            if i<0:
                raise ValueError("Should not be negative")
        return l
   
            
    
student_info = {'name': 'Ani', 'age': 25, "roll": 26, 'email': 'lhamsani@gmail.com', 'married': True, 'leaves': [1,3,4,5,6,7], 'subjects': {'math': 9, 'eng': 10, 'science': 11}}

s = Student(**student_info)

def insert_student_data(student: Student):
    print(f"Inserted the {student.name}, {student.roll} and {student.age} into the database!!!")
    print(student.email)
    print(student.married)
    print()
    for i in student.leaves:
        print("the leaves:", i)
    for d,v in student.subjects.items():
        print("d: ",d,v)
    print(student.subjects["math"], student.subjects["eng"], student.subjects["science"])

insert_student_data(s)

