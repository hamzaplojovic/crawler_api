from fastapi import Depends, APIRouter
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter(
    prefix="/user",
    tags=["Auth"]
)

security = HTTPBasic()


@router.get("/")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": credentials.username, "password": credentials.password}
