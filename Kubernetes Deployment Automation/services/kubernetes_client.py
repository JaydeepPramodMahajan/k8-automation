# from kubernetes import client,config
# #Load kubeconfig (~/.kube/config)
# config.load_kube_config()
# #reads the same kubeconfig file that kubectl uses.
# #AppV1Api() for--> Deployments,ReplicaSet,StatusfulSets 
# apps_v1=client.AppV1Api()
# #CoreV1Api--> Pods,services,configMap,Secreats,Namespaces
# core_v1=client.CoreV1Api()

from kubernetes import client, config

# Load kubeconfig (~/.kube/config)
config.load_kube_config()

# Kubernetes API Clients
apps_v1 = client.AppsV1Api()
core_v1 = client.CoreV1Api()