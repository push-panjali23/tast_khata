from fastapi import FastAPI 
from src.routers import customer
from src.database.connect import engine
from src.database import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(customer.routers)