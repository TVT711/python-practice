from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException

from . import models, schemas
from sqlalchemy import select


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate, company_id: int):
    try:
        fake_hashed_password = user.password + "xxxxxxxx"
        db_user = models.User(
            email=user.email, hash_password=fake_hashed_password, username=user.username,
            first_name=user.first_name, last_name=user.last_name, is_admin=user.is_admin, is_active=user.is_active,
            company_id=company_id
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error creating user: " + str(e)) from e
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error: " + str(e)) from e

    return db_user

def delete_user(db: Session, user_id: int):
    # TODO add more validation to check corresponding tasks that should delete also or throw warning message
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def get_task_by_email(db: Session, email: str):
    # Subquery to fetch the owner_id directly
    subquery = select(models.User.id).where(models.User.email == email).scalar_subquery()

    # Query tasks using the subquery to filter by owner_id
    task = db.query(models.Task).filter(models.Task.owner_id == subquery).first()

    return task


def get_task_by_id(db: Session, task_id: int):
    # TODO
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def create_user_task(db: Session, task: schemas.TaskCreate, user_id: int):
    try:
        db_task = models.Task(**task.dict(), owner_id=user_id)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error creating user: " + str(e)) from e
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error: " + str(e)) from e

    return db_task


def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}


def update_task(db: Session, task_id: int, task_update: schemas.TaskUpdate):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task_update.dict(exclude_unset=True).items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task


def get_company(db: Session, company_id: int):
    return db.query(models.Company).filter(models.Company.id == company_id).first()


def get_companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Company).offset(skip).limit(limit).all()


def delete_company(db: Session, company_id: int):
    # TODO add more validation to check corresponding users that should delete also or throw warning message
    company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    db.delete(company)
    db.commit()
    return {"message": "Company deleted successfully"}


def create_company(db: Session, company: schemas.CompanyCreate):
    try:
        db_company = models.Company(**company.dict())

        db.add(db_company)
        db.commit()
        db.refresh(db_company)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error creating user: " + str(e)) from e
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error: " + str(e)) from e

    return db_company


def update_company(db: Session, company_id: int, company_update: schemas.CompanyUpdate):
    company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    for key, value in company_update.dict(exclude_unset=True).items():
        setattr(company, key, value)
    db.commit()
    db.refresh(company)
    return company
