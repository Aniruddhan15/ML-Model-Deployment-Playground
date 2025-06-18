from fastapi import FastAPI
import json

def newdata():
    with open('Tutorials/patients.json', 'r') as file:
        data2 = json.load(file)
    return data2
    
app = FastAPI()


@app.get('/')
def home():
    return {"message":"Hellow to this new recordof Patients database"}

@app.get('/patientdata')
def patientdata():
    data = newdata()
    
    return data
    
    
'''
def newdata():
    with open('','r') as f:
        data2 = json.load(f)
    return data2


@app.get('/patients')
def patients():
    data = newdata()
    return data

'''