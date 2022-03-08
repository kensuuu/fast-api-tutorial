from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    text: Optional[str] = None
    timestamp: datetime