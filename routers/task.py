from typing import List

from fastapi import APIRouter

from models.task import Task

router = APIRouter()

@router.get("/tasks", status_code=200, tags=["tasks"])
async def get_tasks(user_id: int):
    return {"message": "TODO LIST"}

@router.post("/tasks", status_code=201, tags=["tasks"])
async def create_task(task: Task):
    return {"messge": "作成しました。"}

@router.put("/tasks/{task_id}", status_code=204, tags=["tasks"])
async def update_task(task_id: int):
    return {"message": "更新しました。"}

@router.delete("/tasks/{task_id}", status_code=204, tags=["tasks"])
async def delete_task(task_id: int):
    return {"message": "削除しました。"}