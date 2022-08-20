from typing import Union
from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def read_root():
    response = infoUser()
    return {"items": response }

@app.get("/infoUser/{idUsuario}")
def read_item(idUsuario : int):
    list=infoUser()
    for item in list:
        print(item)
        if item["idUsuario"]==idUsuario:
            return item

def infoUser():
    url='https://62fef1fea85c52ee483e83bb.mockapi.io/authUsers'
    response = requests.get(url, {}, timeout=5)
    return response.json()