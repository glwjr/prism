from pydantic import BaseModel


class MoodBase(BaseModel):
    name: str
    owner_id: str


class MoodCreate(MoodBase):
    pass


class Mood(MoodBase):
    id: int
    name: str
    owner_id: str

    class Config:
        from_attributes = True


class ActivityBase(BaseModel):
    name: str
    owner_id: str


class ActivityCreate(ActivityBase):
    pass


class Activity(ActivityBase):
    id: int
    name: str
    owner_id: str

    class Config:
        from_attributes = True


class EntryBase(BaseModel):
    owner_id: str
    mood_id: str
    activities: list[Activity] = []


class EntryCreate(EntryBase):
    pass


class Entry(BaseModel):
    id: int
    owner_id: str
    mood_id: int
    activities: list[Activity] = []

    class Config:
        from_attributes = True
