from typing import Union
from fastapi import FastAPI
import requests
from prometheus_fastapi_instrumentator import Instrumentator
import logging.config

app = FastAPI()

Instrumentator().instrument(app).expose(app)


logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project. 
                                      # This will get the root logger since no logger in the configuration has this name.


@app.get("/")
def read_root():
    return authUsers()

@app.get("/authUsers/{encryptedToken}")
def read_item(encryptedToken : str):
    list=authUsers()
    for item in list:
        if item["encryptedToken"]==encryptedToken:
            return item

def authUsers():
    url='https://62fef1fea85c52ee483e83bb.mockapi.io/authUsers'
    response = requests.get(url, {}, timeout=5)
    return response.json()