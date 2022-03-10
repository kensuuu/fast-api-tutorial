from fastapi import HTTPException
from models import task
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

def get_tasks(db: Session):
    tasks = db.query(task.Task).all()
    return tasks

def get_task(db: Session, task_id: int):
    try:
        return db.query(task.Task).filter(task.Task.id == task_id)
    except BaseException:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Task is not found.')
    return task