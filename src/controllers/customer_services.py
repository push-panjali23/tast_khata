from src.schemas.schemas import CustomerPayload
from sqlalchemy.orm import Session
from src.database.models import Customer


def get_customer_api(db: Session):
    data = db.query(Customer).all()

    return data


def add_customer_api(payload: CustomerPayload, db: Session):
    entry = Customer(
        customer_name=payload.name,
        mob=payload.mod_no,
        remaining_amount=payload.remaining_amount,
    )

    db.add(entry)
    db.commit()
    return {"message": "customer deatils added"}
