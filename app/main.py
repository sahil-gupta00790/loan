from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.auth import employee , customer
from .routers import Loan_request , collateral , investment , employee_to_do

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
app.include_router(Loan_request.router)
app.include_router(collateral.router)
app.include_router(investment.router)
app.include_router(employee_to_do.router)





