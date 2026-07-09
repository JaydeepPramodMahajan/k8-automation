from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#To Deploy from the website we use the jinja2 

class DeploymentRequest(BaseModel):
    deployment_name: str
    image: str 
    replicas: int
    container_port: int
    service_port: int


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


