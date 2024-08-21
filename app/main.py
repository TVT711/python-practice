from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/companies/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    return crud.create_company(db=db, company=company)


@app.get("/companies/", response_model=list[schemas.Company])
def read_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = crud.get_companies(db, skip=skip, limit=limit)
    return companies


@app.get("/companies/{company_id}", response_model=schemas.Company)
def read_company(company_id: int, db: Session = Depends(get_db)):
    res = crud.get_company(db, company_id=company_id)
    if res is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return res


@app.delete("/companies/{company_id}", response_model=dict)
def delete_company(company_id: int, db: Session = Depends(get_db)):
    return crud.delete_company(db, company_id)


@app.put("/companies/{company_id}", response_model=schemas.Company)
def update_company(company_id: int, company_update: schemas.CompanyUpdate, db: Session = Depends(get_db)):
    return crud.update_company(db, company_id, company_update)


@app.post("/users/{company_id}/", response_model=schemas.User)
def create_user(company_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    # TODO
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user, company_id=company_id)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)


@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user_update)


@app.post("/tasks/{user_id}/", response_model=schemas.Task)
def create_task_for_user(
        user_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)
):
    return crud.create_user_task(db=db, task=task, user_id=user_id)


@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks


@app.get("/tasks/{owner_email}", response_model=schemas.Task)
def read_task_by_email(owner_email: str, db: Session = Depends(get_db)):
    result = crud.get_task_by_email(db, email=owner_email)
    if result is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return result


@app.get("/tasks/{task_id}", response_model=schemas.TaskBase)
def read_task_by_id(task_id: int, db: Session = Depends(get_db)):
    result = crud.get_task_by_id(db, task_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return result


@app.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)


@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, task_update)
