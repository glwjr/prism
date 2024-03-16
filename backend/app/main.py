from typing import Annotated

from fastapi import FastAPI, Security
from utils import VerifyToken

app = FastAPI()
auth = VerifyToken()


@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.get("/private")
def private(auth_result: str = Security(auth.verify)):
    return auth_result