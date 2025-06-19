def insert_patient_data(name: str, age: int):
    
    if type(name) == str and type(age) == int:
        print(f"Inserted the {name} and {age} into the database!!!")
    else:
        raise TypeError("Not the correct datatype")    
        
insert_patient_data("Aniruddhan", 21)


# Pydantic resolves Data Validation and Type Validation

'''
step 1: Build a pydantic class representing ideal schema of the insert_patient_data

step 2: Instantiate the model  with raw input data usually a dictionary or JSON like

step 3: Pass the validated model object to functions or use it throught your codebase

'''

from pydantic import BaseModel, EmailStr, Field, field_validator 
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
    @field_validator('age')
    @classmethod
    def validate_age(cls, age):
        if age%2 == 0:
            raise ValueError("Age should not be even")
        return f"{age} is odd"
            
    
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


from pydantic import BaseModel

class Dog(BaseModel):
    
    breed: str
    years: int
    sound: str
    sleep: float
    
dog1 = {'breed': 'pomarean', 'years': 34, 'sound': 'barkkkk', 'sleep': 4}
d = Dog(**dog1)


def repeat_value(dog: Dog):
    print(f"Hi, I have a dog breed which is {dog.breed} which is {dog.years} old.")
    print(f"It has a sleep time of {dog.sleep} hours and a sound which feels like {dog.sound}")
    
    
repeat_value(d)
