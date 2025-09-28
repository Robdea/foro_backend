from pydantic import BaseModel
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    content: str

class PostOut(BaseModel):
    id: str
    title: str
    author_id: str
    content: str
    created_at: datetime

    
    class Config:
        orm_mode = True