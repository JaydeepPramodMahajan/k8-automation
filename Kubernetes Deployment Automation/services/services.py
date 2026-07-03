from app.schema.structure import AllTasks,InsertTask,UpdateTask
from datetime import datetime


task_list=[]
def create_task(task:InsertTask):
    i=AllTasks(
        U_id=len(task_list)+1,
        Title=task.Title,
        Description=task.Description,
        completed=False,
        created_at=datetime.now(),
    )
    task_list.append(i)
    return i

def displaytask():
    return task_list

def searchid(id:int):
    for i in task_list:
        if i.U_id==id:
            return i
        else:
            return{"Not":"Found"}
        
def currenttask(id:int,task:UpdateTask):
    for i in task_list:
        if i.U_id==id:
            i.Title=task.Title
            i.Description=task.Description
            i.completed=task.completed
        
            return i
        else:
            return{"Not":"Foud"}

        
    
def deletetaskid(id:int):
    for i in task_list:
        if i.U_id==id:
            task_list.remove(i)    
            return {"Removed":"Succesfully"}
    return{"Removed":"Unsucessfuly"}