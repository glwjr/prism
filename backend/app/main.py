from typing import Annotated

from fastapi import FastAPI, Security
from .utils import VerifyToken

app = FastAPI()
auth = VerifyToken()


@app.get("/api/public")
def public():
    return {"message": "Hello World!"}

@app.get("/api/private")
def private(auth_result: str = Security(auth.verify)):
    return auth_result