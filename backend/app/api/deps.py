from fastapi import Depends, Security

from app.core.database import SessionLocal
from app.utils import VerifyToken

auth = VerifyToken()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionDep = Depends(get_db)
AuthDep = Security(auth.verify)
