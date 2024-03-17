import os
from fastapi import FastAPI, Security
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from .utils import VerifyToken

app = FastAPI()
auth = VerifyToken()

origins = [
    os.getenv("LOCAL_ORIGIN"), os.getenv("DEPLOYED_ORIGIN")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/public")
def public():
    return {"message": "Hello World!"}

@app.get("/api/private")
def private(auth_result: str = Security(auth.verify)):
    return auth_result