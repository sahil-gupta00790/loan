from typing import List
from fastapi import APIRouter ,Depends , status ,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session , sessionmaker
from app.database import get_db , Base
from app import oauthemployee, utils , schema
from app.schema import Loan
from sqlalchemy import MetaData , Table
from app.database import SessionLocal , engine , Base
from app.schema import unapproved_loans
from decimal import Decimal
from typing import Any
import json
import psycopg2 as psg
from psycopg2.extras import RealDictCursor
import time
from app.config import settings
from . import  transaction
from app.schema import Transaction

while True:
    try:
        conn=psg.connect(host=settings.database_hostname, database=f'{settings.database_name}', user=f'{settings.database_username}', password=f'{settings.database_password}', cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connection successful")
        break
    except Exception as error:
        print("Database connection failed")
        print("Error", error)
        time.sleep(2)

router=APIRouter(tags=['Employee'])

def custom_encoder(obj: Any):
    if isinstance(obj, Decimal):
        # Convert Decimal to float
        return float(obj)
    elif isinstance(obj, int):
        # Convert NumPy integers to standard Python int
        return int(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

@router.get('/get/loans')
def get_loans(db:Session=Depends(get_db),current_user:int=Depends(oauthemployee.get_current_user)):
    Loans=Base.classes.loan
    return db.query(Loans).all()


@router.get('/get/unapproved')
def get_unapproved(db:Session=Depends(get_db), current_user:int=Depends(oauthemployee.get_current_user)):
   cursor.execute("""SELECT * FROM non_approved_loans""")
   new=cursor.fetchall()
   return new

@router.put('/approve/loan/{id}')
def approve_loan(id:int, db:Session=Depends(get_db), current_user:int=Depends(oauthemployee.get_current_user)):
    Loans=Base.classes.loan
    new=db.query(Loans).filter(Loans.id==id).first()
    if new is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Loan not found")
    
    new.approvval_status="Accepted"
    db.add(new)
    db.commit()
    db.refresh(new)

    LCA=Base.classes.loan_customer_officer_collateral_details
    new=db.query(LCA).filter(LCA.loan_id==id).first()
    new.officer_id=current_user
    db.add(new)
    db.commit()
    db.refresh(new)
    
    transaction.addTransaction(sender_id=current_user,amount=new.loan_amount)

    return {"message":"Loan approved"}

@router.get('/get/not_paid')
def get_not_paid(db:Session=Depends(get_db), current_user:int=Depends(oauthemployee.get_current_user)):
    cursor.execute("""SELECT * FROM customer_who_did_not_pay""")
    new=cursor.fetchall()
    return new


    
    