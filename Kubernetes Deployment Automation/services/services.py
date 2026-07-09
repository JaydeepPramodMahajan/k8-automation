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

#-----------------------------------------------------
#---------------------------------------------------------

from pathlib import Path
from jinja2 import Environment, FileSystemLoader

BASE_DIR = Path(__file__).resolve().parent.parent

template_dir = BASE_DIR / "templates"
generated_dir = BASE_DIR / "generated"

env = Environment(loader=FileSystemLoader(template_dir))


def generate_deployment_yaml(data):
    template = env.get_template("deployment.yaml.j2")#Loading the deployment.yaml.j2 
    service_template = env.get_template("service.yaml.j2")
    output = template.render(# Data will be in JSON formate, And to take the values of server to the {{}} value we are using this
        deployment_name=data.deployment_name,
        image=data.image,
        replicas=data.replicas,
        container_port=data.container_port
    )

    generated_dir.mkdir(exist_ok=True)

    output_file = generated_dir / "deployment.yaml"

    with open(output_file, "w") as file:
        file.write(output)

    return str(output_file)

def generate_service_yaml(data):
    template = env.get_template("service.yaml.j2")

    output = template.render(
        deployment_name=data.deployment_name,
        service_port=data.service_port,
        container_port=data.container_port
    )

    generated_dir.mkdir(exist_ok=True)

    output_file = generated_dir / "service.yaml"

    with open(output_file, "w") as file:
        file.write(output)

    return str(output_file)



import subprocess

def apply_yaml(file_path):
    result = subprocess.run(
        ["kubectl", "apply", "-f", file_path],
        capture_output=True,
        text=True
    )

    return result.stdout, result.stderr



def rollout_status(deployment_name):
    result = subprocess.run(
        [
            "kubectl",
            "rollout",
            "status",
            f"deployment/{deployment_name}",
            "--timeout=120s"
        ],
        capture_output=True,
        text=True
    )

    return result.stdout, result.stderr


def get_pods(deployment_name):
    result = subprocess.run(
        [
            "kubectl",
            "get",
            "pods",
            "-l",
            f"app={deployment_name}",
            "-o",
            "wide"
        ],
        capture_output=True,
        text=True
    )

    return result.stdout


def get_service(deployment_name):
    result = subprocess.run(
        [
            "kubectl",
            "get",
            "service",
            f"{deployment_name}-service"
        ],
        capture_output=True,
        text=True
    )

    return result.stdout
    
import json

def get_all_deployments():
    result = subprocess.run(
        [
            "kubectl",
            "get",
            "deployments",
            "-o",
            "json"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return {"error": result.stderr}

    return json.loads(result.stdout)