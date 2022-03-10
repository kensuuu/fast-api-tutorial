from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.mysql import TIMESTAMP
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Column(
        Integer,
        primary_key=True,
        index=True
    )

    title: Column(
        String(128),
        nullable=False
    )

    text: Column(
        Text,
        nullable=True
    )

    created_at: Column(
        TIMESTAMP,
        nullable=False,
        server_default=text('current_timestamp')
    )
