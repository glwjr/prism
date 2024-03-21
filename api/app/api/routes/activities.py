from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.api.deps import SessionDep, AuthDep
from app import crud, schemas


router = APIRouter()


@router.get("/", response_model=list[schemas.Activity])
def read_user_activities(db: Session = SessionDep, auth: str = AuthDep):
    id = auth["sub"]
    return crud.get_activities_by_user_id(db=db, user_id=id)


@router.post("/", response_model=schemas.Activity)
def create_activity_for_user(
    name: str,
    db: Session = SessionDep,
    auth: str = AuthDep,
):
    id = auth["sub"]
    return crud.create_user_activity(db=db, user_id=id, name=name)
