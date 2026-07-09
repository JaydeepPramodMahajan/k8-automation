from fastapi import APIRouter,status
from app.schema.structure import DeploymentRequest,AllTasks,InsertTask,UpdateTask
from services.services import get_all_deployments,get_service,get_pods,rollout_status,apply_yaml,generate_service_yaml,generate_deployment_yaml,create_task,displaytask,searchid,currenttask,deletetaskid

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
@router.delete("/deployment/{deployment_name}")
def remove_deployment(deployment_name: str):

    delete_deployment(deployment_name)

    delete_service("k8-service")

    return {
        "message":"Deleted Successfully"
    }

#--------------------------------------------------------
#----------------------------------------------------------
@router.post("/deploy")
def deploy(data: DeploymentRequest):
   deployment_file = generate_deployment_yaml(data)
   service_file = generate_service_yaml(data)

   apply_yaml(deployment_file)
   apply_yaml(service_file)

   rollout, rollout_error = rollout_status(data.deployment_name)

   pods = get_pods(data.deployment_name)

   service = get_service(data.deployment_name)

   return {
    "message": "Deployment Successful",
    "rollout": rollout,
    "pods": pods,
    "service": service
}

@router.get("/deployments")
def list_deployments():
    return get_all_deployments()
from services.deployment_service import list_deployments
from services.deployment_service import list_deployments

@router.get("/deployments")
def get_deployments():
    return list_deployments()

from app.models.deployment import ScaleRequest
from services.deployment_service import scale_deployment

@router.put("/scale")
def scale(data: ScaleRequest):

    return scale_deployment(data)

from app.models.deployment import UpdateImageRequest
from services.deployment_service import update_image,restart_deployment,get_deployment

@router.put("/update-image")
def update(data: UpdateImageRequest):

    return update_image(data)
@router.post("/restart/{deployment_name}")
def restart(deployment_name: str):

    return restart_deployment(deployment_name)

@router.get("/deployment/{deployment_name}")
def deployment_details(deployment_name: str):

    return get_deployment(deployment_name)

from services.pod_service import list_pods,get_pod_details,get_pod_logs,delete_pod


router2=APIRouter(prefix="/pods",tags=["Pods"])
@router2.get("/list")
def pods():

    return list_pods()


@router2.get("/{pod_name}")
def pod_details(pod_name: str):

    return get_pod_details(pod_name)
@router2.get("/{pod_name}/logs")
def pod_logs(pod_name: str):

    return get_pod_logs(pod_name)
@router2.delete("/{pod_name}")
def delete(pod_name: str):

    return delete_pod(pod_name)