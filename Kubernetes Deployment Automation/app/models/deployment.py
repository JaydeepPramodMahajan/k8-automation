from pydantic import BaseModel

class ScaleRequest(BaseModel):
    deployment_name: str
    replicas: int

class UpdateImageRequest(BaseModel):
    deployment_name: str
    image: str