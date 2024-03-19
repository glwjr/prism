from sqlalchemy.orm import Session

from app import models


def get_moods_by_user_id(db: Session, user_id: str):
    return db.query(models.Mood).filter(models.Mood.owner_id == user_id).all()


def create_user_mood(db: Session, user_id: str, name: str):
    db_mood = models.Mood(owner_id=user_id, name=name)
    db.add(db_mood)
    db.commit()
    db.refresh(db_mood)
    return db_mood


def get_activities_by_user_id(db: Session, user_id: str):
    return db.query(models.Activity).filter(models.Activity.owner_id == user_id).all()


def create_user_activity(db: Session, user_id: str, name: str):
    db_activity = models.Activity(owner_id=user_id, name=name)
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


def get_entries_by_user_id(db: Session, user_id: str):
    return db.query(models.Entry).filter(models.Entry.owner_id == user_id).all()


def create_user_entry(
    db: Session, user_id: str, mood_id: str, activities: list[models.Activity]
):
    db_entry = models.Entry(owner_id=user_id, mood_id=mood_id)
    db_entry.activities.extend(activities)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry
