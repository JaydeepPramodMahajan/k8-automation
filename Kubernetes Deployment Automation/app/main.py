from fastapi import FastAPI
from dotenv import load_dotenv
import os
load_dotenv()
from app.core.config import get_version as g_v
from app.api.routers import router,router2 
from app.api.service_router import router1
app=FastAPI()

@app.get("/")
async def dashbord():
    return {"message":"This is the dashboard. Project"}
@app.get("/status")
async def health():
    return {"Status":"Website is running"}
version=os.getenv("version")
@app.get("/version")
async def get_version():
    return{"Version":version}

app.include_router(router)
app.include_router(router1)
app.include_router(router2)