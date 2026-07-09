from kubernetes.client.rest import ApiException
from services.kubernetes_client import core_v1


def list_services():

    try:

        services = core_v1.list_namespaced_service(
            namespace="default"
        )

        result = []

        for service in services.items:

            ports = []

            for port in service.spec.ports:

                ports.append({

                    "port": port.port,

                    "target_port": port.target_port,

                    "protocol": port.protocol

                })

            result.append({

                "name": service.metadata.name,

                "type": service.spec.type,

                "cluster_ip": service.spec.cluster_ip,

                "external_ip": service.status.load_balancer.ingress
                    if service.status.load_balancer.ingress
                    else None,

                "selector": service.spec.selector,

                "ports": ports

            })

        return result

    except ApiException as e:

        return {
            "error": e.body
        }
    
from kubernetes.client.rest import ApiException

def get_service_details(service_name: str):

    try:

        service = core_v1.read_namespaced_service(
            name=service_name,
            namespace="default"
        )

        ports = []

        for port in service.spec.ports:

            ports.append({
                "name": port.name,
                "protocol": port.protocol,
                "port": port.port,
                "target_port": port.target_port,
                "node_port": port.node_port
            })

        return {

            "name": service.metadata.name,

            "namespace": service.metadata.namespace,

            "type": service.spec.type,

            "cluster_ip": service.spec.cluster_ip,

            "external_ip":
                service.status.load_balancer.ingress
                if service.status.load_balancer.ingress
                else None,

            "selector": service.spec.selector,

            "session_affinity": service.spec.session_affinity,

            "ports": ports,

            "created_at": service.metadata.creation_timestamp
        }

    except ApiException as e:

        return {
            "error": e.body
        }
    
from kubernetes.client.rest import ApiException

def delete_service(service_name: str):

    try:

        core_v1.delete_namespaced_service(
            name=service_name,
            namespace="default"
        )

        return {
            "message": f"Service '{service_name}' deleted successfully."
        }

    except ApiException as e:

        return {
            "error": e.body
        }