from fastapi import APIRouter,status
from app.schema.structure import AllTasks,InsertTask,UpdateTask
from services.services import create_task,displaytask,searchid,currenttask,deletetaskid

router=APIRouter(prefix="/tasks",tags=["Tasks"])

@router.post("/insert",response_model=AllTasks,status_code=status.HTTP_201_CREATED,)
def insert_data(insert_task:InsertTask):
    return create_task(insert_task)

@router.get("/All",response_model=list[AllTasks])
def get_all_tasks():
    return displaytask()

@router.get("/search/{search_id}",response_model=AllTasks,)
def search(search_id:int):
    return searchid(search_id)
    
@router.put("/update/{search_id}",response_model=AllTasks,status_code=status.HTTP_201_CREATED,)
def update(search_id:int,task:UpdateTask):
    return currenttask(search_id,task)

@router.delete("/delete/{search_id}",status_code=status.HTTP_204_NO_CONTENT,)
def deletetask(search_id:int):
    return deletetaskid(id)


