
from fastapi import FastAPI, Path, HTTPException, Query
import json

def load_data():
    with open('Tutorials/patients.json','r') as f:
        data = json.load(f)
    return data

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Hellow!!!! Welcome to Patient Management system!!"}

@app.get('/about')
def about():
    return {"message": "This is about page of Fully functional api to manage patient records!"}


@app.get('/view')
def view():
    data = load_data()
    
    return data
    
@app.get('/specific/{patient_id}')
def specific(patient_id: str = Path(..., description= 'Id of the patient in the DataBase', example= 'P002')):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code= 404, detail="Patient not found")
    
    
@app.get('/sorty')
def sorty(sort_by: str = Query(..., decription='Sorting done by height, weight and BMI'), order: str = Query('asc', description= "Sorting in ascending order")):
    valid_fields = ['height', 'weight', 'BMI']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code= 400, detail="Invalid sorting field")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code= 400, detail="Invalid sorting order")  
    
    data = load_data()
    sort_order = True if order=='desc' else False
    sorted_data= sorted(data.values(), key= lambda x: x.get(sort_by,0), reverse=sort_order) 
    
    return sorted_data

    
    
from fastapi import FastAPI, Path, HTTPException, Query
import json

def load_data():
    with open('patients.json', 'r') as f:
        da = json.load(f)
         
    return da

@app.get('/patients')
def patients():
    data = load_data()
    return data

@app.get('/specificpatient/{id}')
def specificpatients(id: str = Path(..., description="Something", example="P002")):
    data = load_data()
    
    if id in data:
        return data[id]
    else:
        raise HTTPException(status_code =400, detail='Patient not found' )
    
   

        
''' Dry run

from fastapi import FastAPI
import json

def newdata():
    with open('patients.json','r') as file:
        d = json.load(file)z
    return d

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Hellow!!!! Welcome to Patient Management system!!"}

@app.get('/patients')
def patients():
    data = load_data()
    return data

@app.get('/specificpatient/{id}')
def specificpatient(id: str):
    data = load_data()
    
    if id == data:
        return data[id]
    else:
        return {"message": "Patient not found in the data"}
    


'''
