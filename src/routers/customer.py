from fastapi import APIRouter, Depends
from src.controllers.customer_services import get_customer_api, add_customer_api
from src.schemas.schemas import CustomerPayload
from src.database.connect import get_db
from sqlalchemy.orm import Session

routers = APIRouter(
    tags=[
        "Customers",
    ]
)


@routers.get("/customer")
def get_cutomers(db: Session = Depends(get_db)):

    return get_customer_api(db)


@routers.post("/customer")
def add_customer(payload: CustomerPayload = Depends(), db: Session = Depends(get_db)):

    return add_customer_api(payload, db)
