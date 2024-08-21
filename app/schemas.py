from pydantic import BaseModel


class TaskBase(BaseModel):
    summary: str
    description: str | None = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    owner_id: int | None = None

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    is_admin: bool
    is_active: bool
    company_id: int


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
    tasks: list[Task] = []

    class Config:
        orm_mode = True


class CompanyBase(BaseModel):
    name: str
    description: str
    mode: int
    rating: int


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(CompanyBase):
    pass


class Company(CompanyBase):
    id: int
    users: list[User] = []

    class Config:
        orm_mode = True
