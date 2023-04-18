from fastapi import Depends, FastAPI,HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine



app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.get('/users/', response_model = list[schemas.User])
def get_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
	users = crud.get_users(db = db, skip = skip, limit = limit)
	return users

@app.get('/users/{user_id}', response_model = schemas.User)
def get_user(user_id: int,db: Session = Depends(get_db)):
	user = crud.get_user(db = db, user_id = user_id)
	if user is None:
		raise HTTPException(status_code=404, detail="User not found")
	return user

@app.post('/users/', response_model = schemas.User)
def create_user(user:schemas.UserCreate,db: Session = Depends(get_db)):
	db_user = crud.create_user(db = db, user = user)
	return db_user


@app.get('/orgs/', response_model = list[schemas.Org])
def get_orgs(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
	orgs = crud.get_orgs(db = db, skip = skip, limit = limit)
	return orgs

@app.get('/orgs/{org_id}', response_model = schemas.Org)
def get_org(org_id: int,db: Session = Depends(get_db)):
	org = crud.get_org(db = db, org_id = org_id)
	if org is None:
		raise HTTPException(status_code=404, detail="Org not found")
	return org

@app.post('/orgs/', response_model = schemas.Org)
def create_org(org:schemas.OrgCreate,db: Session = Depends(get_db)):
	db_org = crud.create_org(db = db, org = org)
	return db_org
