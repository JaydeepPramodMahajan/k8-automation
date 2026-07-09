from fastapi import APIRouter
from services.service_service import list_services,get_service_details,delete_service

router1 = APIRouter(
    prefix="/services",
    tags=["Services"]
)


@router1.get("")
def services():

    return list_services()
@router1.get("/{service_name}")
def service_details(service_name: str):

    return get_service_details(service_name)

@router1.delete("/{service_name}")
def delete(service_name: str):

    return delete_service(service_name)