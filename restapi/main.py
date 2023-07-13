from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import json

app = FastAPI()

'''
Basic tests with FastAPI, get and post request 

@app.get('/')
def hello():
    return {"Hello" : "World"}

@app.post('/')
def hello_post():
    return {"Success" : "Post"}

@app.get('/something')
def something():
    return {"Data" : "Something"}

'''

class Person(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str

with open('people.json', 'r') as f:
    people = json.load(f)['people']

@app.get('/person/{p_id}')
def get_person(p_id:int) :
    person = [p for p in people if p ['id'] == p_id]
    return person[0] if len(person) > 0 else {}

def search_person(age: Optional[int] = Query(None, title="Age", description="The age to filter for"), 
                  name: Optional[str] = Query(None, title="Name", description="The name to filter for"))
    people1 = [p for p in people if p['age'] == age]

    if name is None:
        if age is None:
            return people
        else:
            return people1


