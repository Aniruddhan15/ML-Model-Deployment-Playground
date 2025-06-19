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

from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional


class Student(BaseModel):
    
    name: str
    age: int
    roll: float
    email: EmailStr
    married: bool
    leaves: List[int]
    # leaves: Optional[List[int]] = None this means optional printing, so doesnt print as it becomes optional
    subjects: Dict[str, int]
    
    
student_info = {'name': 'Ani', 'age': 21, "roll": 26, 'email': 'lhamsani@gmail.com', 'married': True, 'leaves': [2,3,4,5,6,7], 'subjects': {'math': 9, 'eng': 10, 'science': 11}}

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
