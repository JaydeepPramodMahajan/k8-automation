from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AllTasks(BaseModel):
    U_id: int
    Title:str
    Description:Optional[str]=None
    completed:bool
    created_at:datetime

class InsertTask(BaseModel):
    Title:str
    Description:Optional[str]=None

class UpdateTask(BaseModel):
    Title:str
    Description:Optional[str]=None
    completed:bool


