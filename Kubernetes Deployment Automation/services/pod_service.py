from services.kubernetes_client import core_v1
from kubernetes.client.rest import ApiException


def list_pods():

    try:

        pods = core_v1.list_namespaced_pod(
            namespace="default"
        )

        result = []

        for pod in pods.items:

            result.append({

                "name": pod.metadata.name,

                "namespace": pod.metadata.namespace,

                "status": pod.status.phase,

                "node": pod.spec.node_name,

                "pod_ip": pod.status.pod_ip,

                "host_ip": pod.status.host_ip,

                "restart_count":
                    pod.status.container_statuses[0].restart_count
                    if pod.status.container_statuses
                    else 0,

                "image":
                    pod.spec.containers[0].image

            })

        return result

    except ApiException as e:

        return {"error": e.body}
    
from kubernetes.client.rest import ApiException
from services.kubernetes_client import core_v1

def get_pod_details(pod_name: str):

    try:

        pod = core_v1.read_namespaced_pod(
            name=pod_name,
            namespace="default"
        )

        return {

            "name": pod.metadata.name,

            "namespace": pod.metadata.namespace,

            "status": pod.status.phase,

            "pod_ip": pod.status.pod_ip,

            "host_ip": pod.status.host_ip,

            "node": pod.spec.node_name,

            "start_time": pod.status.start_time,

            "qos_class": pod.status.qos_class,

            "service_account": pod.spec.service_account_name,

            "containers": [

                {

                    "name": container.name,

                    "image": container.image,

                    "port": container.ports[0].container_port if container.ports else None

                }

                for container in pod.spec.containers

            ]

        }

    except ApiException as e:

        return {
            "error": e.body
        }
from kubernetes.client.rest import ApiException

def get_pod_logs(pod_name: str):

    try:

        logs = core_v1.read_namespaced_pod_log(
            name=pod_name,
            namespace="default"
        )

        return {
            "pod_name": pod_name,
            "logs": logs
        }

    except ApiException as e:

        return {
            "error": e.body
        }
    
from kubernetes.client.rest import ApiException

def delete_pod(pod_name: str):

    try:

        core_v1.delete_namespaced_pod(
            name=pod_name,
            namespace="default"
        )

        return {
            "message": f"Pod '{pod_name}' deleted successfully."
        }

    except ApiException as e:

        return {
            "error": e.body
        }