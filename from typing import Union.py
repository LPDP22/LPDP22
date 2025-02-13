from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return(1: 2)

#comando para executar no terminal:
#> pip install "fastapi[standard]"
# fastapi dev main.py