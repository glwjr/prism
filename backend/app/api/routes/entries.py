from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.api.deps import SessionDep, AuthDep
from app import crud, schemas


router = APIRouter()


@router.get("/", response_model=list[schemas.Entry])
def read_user_entries(db: Session = SessionDep, auth: str = AuthDep):
    id = auth["sub"]
    return crud.get_entries_by_user_id(db=db, user_id=id)


@router.post("/", response_model=schemas.Entry)
def create_entry_for_user(
    mood_id: int,
    activity_ids: list[int],
    db: Session = SessionDep,
    auth: str = AuthDep,
):
    id = auth["sub"]
    return crud.create_user_entry(
        db=db, user_id=id, mood_id=mood_id, activity_ids=activity_ids
    )
