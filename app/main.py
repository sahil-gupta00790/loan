from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.auth import employee , customer

from .database import engine

app=FastAPI()




app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

app.include_router(employee.router)
app.include_router(customer.router)





