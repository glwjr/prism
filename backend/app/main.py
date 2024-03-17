import os
from fastapi import Depends, FastAPI, Security
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from .utils import VerifyToken
from . import crud, models, schemas
from .core.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/public")
def public():
    return {"message": "Hello World!"}


@app.get("/api/private")
def private(auth_result: str = Security(auth.verify)):
    return auth_result


@app.get("/api/moods", response_model=list[schemas.Mood])
def read_user_moods(db: Session = Depends(get_db), auth_result: str = Security(auth.verify)):
    id = auth_result["sub"]
    return crud.get_moods_by_user_id(db=db, user_id=id)


@app.post("/api/moods", response_model=schemas.Mood)
def create_mood_for_user(name: str, mood: schemas.MoodCreate, db: Session = Depends(get_db), auth_result: str = Security(auth.verify)):
    id = auth_result["sub"]
    return crud.create_user_mood(db=db, mood=mood, user_id=id, name=name)