#Test the Connection, whole code
from services.kubernetes_client import apps_v1

def list_deployments():
    deployments=apps_v1.list_namespaced_deployment(
        namespace="default"
    )
    result=[]

    for deployment in deployments.items:
        result.append({
            "name": deployment.metadata.name,
            "replicas": deployment.spec.replicas,
            "available": deployment.status.available_replicas,
            "image": deployment.spec.template.spec.containers[0].image
        })

    return result

from kubernetes.client.rest import ApiException
from services.kubernetes_client import apps_v1, core_v1


def delete_deployment(deployment_name: str):

    try:

        apps_v1.delete_namespaced_deployment(
            name=deployment_name,
            namespace="default"
        )

        return {
            "message": f"{deployment_name} deleted successfully"
        }

    except ApiException as e:

        return {
            "error": e.body
        }
    
def delete_service(service_name: str):

    try:

        core_v1.delete_namespaced_service(
            name=service_name,
            namespace="default"
        )

        return {
            "message": f"{service_name} deleted"
        }

    except ApiException as e:

        return {
            "error": e.body
        }
    
from kubernetes.client.rest import ApiException
from services.kubernetes_client import apps_v1

def scale_deployment(data):

    try:

        body = {
            "spec": {
                "replicas": data.replicas
            }
        }

        apps_v1.patch_namespaced_deployment_scale(
            name=data.deployment_name,
            namespace="default",
            body=body
        )

        return {
            "message": f"{data.deployment_name} scaled to {data.replicas} replicas"
        }

    except ApiException as e:
        return {
            "error": e.body
        }
    
from kubernetes.client.rest import ApiException
from services.kubernetes_client import apps_v1

def update_image(data):

    try:

        body = {
            "spec": {
                "template": {
                    "spec": {
                        "containers": [
                            {
                                "name": "k8-automation",
                                "image": data.image
                            }
                        ]
                    }
                }
            }
        }

        apps_v1.patch_namespaced_deployment(
            name=data.deployment_name,
            namespace="default",
            body=body
        )

        return {
            "message": "Rolling Update Started"
        }

    except ApiException as e:

        return {
            "error": e.body
        }
    
from kubernetes.client.rest import ApiException
from datetime import datetime

def restart_deployment(deployment_name: str):

    try:

        body = {
            "spec": {
                "template": {
                    "metadata": {
                        "annotations": {
                            "kubectl.kubernetes.io/restartedAt":
                                datetime.utcnow().isoformat()
                        }
                    }
                }
            }
        }

        apps_v1.patch_namespaced_deployment(
            name=deployment_name,
            namespace="default",
            body=body
        )

        return {
            "message": "Deployment restarted successfully"
        }

    except ApiException as e:
        return {
            "error": e.body
        }
    
from kubernetes.client.rest import ApiException
from services.kubernetes_client import apps_v1

def get_deployment(deployment_name: str):

    try:

        deployment = apps_v1.read_namespaced_deployment(
            name=deployment_name,
            namespace="default"
        )

        return {
            "name": deployment.metadata.name,
            "namespace": deployment.metadata.namespace,
            "replicas": deployment.spec.replicas,
            "available_replicas": deployment.status.available_replicas,
            "ready_replicas": deployment.status.ready_replicas,
            "updated_replicas": deployment.status.updated_replicas,
            "image": deployment.spec.template.spec.containers[0].image,
            "container_name": deployment.spec.template.spec.containers[0].name,
            "strategy": deployment.spec.strategy.type,
            "created_at": deployment.metadata.creation_timestamp,
            "labels": deployment.metadata.labels,
            "annotations": deployment.metadata.annotations
        }

    except ApiException as e:

        return {
            "error": e.body
        }
#----------------------------------------------
#--------------------------------------------