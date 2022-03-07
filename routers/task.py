from datetime import datetime
from typing import Optional, List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Task(BaseModel):
    id: int
    title: str
    text: Optional[str] = None
    timestamp: datetime

@router.get("/tasks", response_model=List[Task], status_code=200, tags=["tasks"])
async def get_tasks(user_id: int):
    return List[Task]

@router.post("/tasks", status_code=201, tags=["tasks"])
async def create_task(task: Task):
    return {"messge": "作成しました。"}

@router.put("/tasks/{task_id}", status_code=204, tags=["tasks"])
async def update_task(task_id: int):
    return {"message": "更新しました。"}

@router.delete("/tasks/{task_id}", status_code=204, tags=["tasks"])
async def delete_task(task_id: int):
    return {"message": "削除しました。"}