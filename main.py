from typing import Union
from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def read_root():
    response = infoUser()
    return {"items": response }

@app.get("/authUsers/{internalId}")
def read_item(internalId : str):
    list=infoUser()
    for item in list:
        print(item)
        if item["internalId"]==internalId:
            return item

def infoUser():
    url='https://62fef1fea85c52ee483e83bb.mockapi.io/authUsers'
    response = requests.get(url, {}, timeout=5)
    return response.json()