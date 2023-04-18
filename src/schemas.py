from pydantic import BaseModel

class OrgBase(BaseModel):
	name : str

class OrgCreate(OrgBase):
	pass

class Org(OrgBase):
	id: int
	admin_id: int | None = None

	class Config:
		orm_mode = True





class UserBase(BaseModel):
	images : str
	bio : str
	country : str
	is_verified : bool
	linkedin_link : str
	git_link : str
	stackexchange_link : str
	timezone : str
	rank : int


class UserCreate(UserBase):
	pass

class User(UserBase):
	id: int
	orgs: list[Org] = []

	class Config:
		orm_mode = True

