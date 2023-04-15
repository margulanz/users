from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
	return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
	return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
	db_user = models.User(
		image = user.image,
		bio = user.bio,
		country = user.country,
		is_verified = user.is_verified,
	    linkedin_link = user.linkedin_link,
	    git_link = user.git_link,
	    stackexchange_link = user.stackexchange_link,
	    timezone = user.timezone,
	    rank = user.rank
	)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user


def get_org(db: Session, org_id: int):
	return db.query(models.Org).filter(models.Org.id == org_id).first()


def get_orgs(db: Session, skip: int = 0, limit: int = 100):
	return db.query(models.Org).offset(skip).limit(limit).all()

def create_org(db: Session, org: schemas.OrgCreate):
	db_org = models.Org(
		name = org.name
	)
	db.add(db_org)
	db.commit()
	db.refresh(db_org)
	return db_org