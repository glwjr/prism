from fastapi import APIRouter, HTTPException

router = APIRouter()


# @router.get("/api/moods", response_model=list[schemas.Mood])
# def read_user_moods(db: Session = Depends(get_db), auth_result: str = Security(auth.verify)):
#     id = auth_result["sub"]
#     return crud.get_moods_by_user_id(db=db, user_id=id)


# @router.post("/api/moods", response_model=schemas.Mood)
# def create_mood_for_user(name: str, mood: schemas.MoodCreate, db: Session = Depends(get_db), auth_result: str = Security(auth.verify)):
#     id = auth_result["sub"]
#     return crud.create_user_mood(db=db, mood=mood, user_id=id, name=name)