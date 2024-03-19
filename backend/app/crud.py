from sqlalchemy.orm import Session

from app import models, schemas


def get_moods_by_user_id(db: Session, user_id: str):
    return db.query(models.Mood).filter(models.Mood.owner_id == user_id).all()


def get_activities_by_user_id(db: Session, user_id: str):
    return db.query(models.Activity).filter(models.Activity.owner_id == user_id).all()


def get_entries_by_user_id(db: Session, user_id: str):
    return db.query(models.Entry).filter(models.Entry.owner_id == user_id).all()


def create_user_mood(db: Session, mood: schemas.MoodCreate, user_id: str, name: str):
    db_mood = models.Mood(owner_id=user_id, name=name)
    db.add(db_mood)
    db.commit()
    db.refresh(db_mood)
    return db_mood
