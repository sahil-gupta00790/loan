from typing import List
from fastapi import APIRouter ,Depends , status ,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db , Base
from app import oauthcustomer, utils , schema
from app.schema import Loan , Transaction
from . import transaction
router=APIRouter(tags=['Investment'])

@router.post('/investment/add')
def add_investment(investment:schema.Investment , db:Session=Depends(get_db),get_current_user:int=Depends(oauthcustomer.get_current_user)):
    Investment=Base.classes.investment
    new_investment=Investment(amount=investment.amount,duration=investment.duration,interest_rate=investment.interest_rate,customer_id=get_current_user,amount_to_be_paid=0)
    db.add(new_investment)
    db.commit()
    db.refresh(new_investment)
    
    transaction.addTransaction(sender_id=get_current_user,amount=new_investment.amount)
    return {"message":"Investment added successfully"}

@router.get('/investment/all')
def get_investment( db:Session=Depends(get_db),get_current_user:int=Depends(oauthcustomer.get_current_user)):
    Investment=Base.classes.investment
    investment=db.query(Investment).filter(Investment.customer_id==get_current_user).all()
    return investment

@router.get('/investment/{id}')
def get_investment_by_id(id:int, db:Session=Depends(get_db), get_current_user:int=Depends(oauthcustomer.get_current_user)):
    Investment=Base.classes.investment
    investment=db.query(Investment).filter(Investment.id==id).first()
    if not investment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Investment with id {id} not found")
    return investment

@router.delete('/investment/{id}')
def delete_investment(id:int, db:Session=Depends(get_db), get_current_user:int=Depends(oauthcustomer.get_current_user)):
    Investment=Base.classes.investment
    investment=db.query(Investment).filter(Investment.id==id).first()
    if not investment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Investment with id {id} not found")
    db.delete(investment)
    db.commit()
    return {"message":"Investment deleted,amount will be reverted in 1-2 days"}

@router.put('/investment/update/{id}')
def update_investment(id:int, investment:schema.Investment, db:Session=Depends(get_db), get_current_user:int=Depends(oauthcustomer.get_current_user)):
    Investment=Base.classes.investment
    investment_to_update=db.query(Investment).filter(Investment.id==id).first()
    if investment_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Investment not found")
    if investment_to_update.customer_id != get_current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")
    #investment_to_update.amount=investment.amount
    investment_to_update.duration=investment.duration
    #investment_to_update.interest_rate=investment.interest_rate
    db.add(investment_to_update)
    db.commit()
    db.refresh(investment_to_update)
    return investment_to_update