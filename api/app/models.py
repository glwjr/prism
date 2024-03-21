from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from app.core.database import Base


entry_activity_table = Table(
    "entry_activity",
    Base.metadata,
    Column("entry_id", ForeignKey("entries.id"), primary_key=True),
    Column("activity_id", ForeignKey("activities.id"), primary_key=True),
)


class Mood(Base):
    __tablename__ = "moods"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner_id = Column(String)

    entries = relationship("Entry", back_populates="mood")


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner_id = Column(String)

    entries = relationship(
        "Entry", secondary=entry_activity_table, back_populates="activities"
    )


class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    owner_id = Column(String)
    mood_id = Column(Integer, ForeignKey("moods.id"))

    mood = relationship("Mood", back_populates="entries")
    activities = relationship(
        "Activity", secondary=entry_activity_table, back_populates="entries"
    )
