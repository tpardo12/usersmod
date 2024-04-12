import random
import time
from typing import Union

import uuid
from faker import Faker
from fastapi import FastAPI
from models import usuario

app = FastAPI()
fake = Faker("es_CO")
usuarios = []
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#put
@app.post('/saveuser')
def save_user(post:usuario.User):
    time.sleep(random.uniform(0.5, 2))
    usuarios.append( usuario.User(id= str(uuid.uuid4()), name= fake.name(), email=fake.email(), phone_number=5448845 ))
    print(usuarios)
    return 'recived'

#update
@app.put('/users/update/{user_id}')
def update_user(user_id: str, updateduser: usuario.User):
  time.sleep(random.uniform(0.5, 2))
  ''''
    for index, users in enumerate (usuarios):
        if usuarios["id"] == user_id:
            usuarios[index]["name"] =updateduser.name
            usuarios[index]["email"] = updateduser.email
            usuarios[index]["phone_number"] = updateduser.phone_number
            return None
    '''
  return usuario.User(id= user_id, name= fake.name(), email=fake.email(), phone_number=5448845 )
  
#get
@app.get('/users/{user_id}')
def get_user(user_id:str):
    time.sleep(random.uniform(0.5, 2))
    return usuario.User(id= user_id, name= fake.name(), email=fake.email(), phone_number=5448845 )
