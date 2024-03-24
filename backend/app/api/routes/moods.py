from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.api.deps import SessionDep, AuthDep
from app import crud, schemas

router = APIRouter()


@router.get("/", response_model=list[schemas.Mood])
def read_user_moods(db: Session = SessionDep, auth: str = AuthDep):
    id = auth["sub"]
    return crud.get_moods_by_user_id(db=db, user_id=id)


@router.post("/", response_model=schemas.Mood)
def create_mood_for_user(
    name: str,
    db: Session = SessionDep,
    auth: str = AuthDep,
):
    id = auth["sub"]
    return crud.create_user_mood(db=db, user_id=id, name=name)
