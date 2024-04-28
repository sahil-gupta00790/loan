from typing import List
from fastapi import APIRouter ,Depends , status ,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db , Base
from app import oauthcustomer, utils , schema
from app.schema import Loan

router=APIRouter(tags=['Collateral'])



@router.post('/collateral/insert')
def addCollateral(collateral:schema.Collateral,get_current_user:int=Depends(oauthcustomer.get_current_user),db:Session=Depends(get_db)):
    Collateral=Base.classes.collateral
    new_req=Collateral(description=collateral.description,  value=collateral.collateral_value,customer_id=get_current_user)
    db.add(new_req)
    db.commit()
    db.refresh(new_req)
    return new_req

@router.get('/collateral/get')
def getloanCollateral(get_current_user:int=Depends(oauthcustomer.get_current_user), db:Session=Depends(get_db)):
    Collateral=Base.classes.collateral
    collateral=db.query(Collateral).filter(Collateral.customer_id==get_current_user).all()
    if collateral is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Collateral not found")
    return collateral



@router.delete('/collateral/delete/{id}')
def deleteCollateral(id:int,get_current_user:int=Depends(oauthcustomer.get_current_user), db:Session=Depends(get_db)):
    Collateral=Base.classes.collateral
    collateral=db.query(Collateral).filter(Collateral.id==id).first()
    if collateral is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Collateral not found")
    if collateral.customer_id != get_current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")
    Lca=Base.classes.loan_customer_officer_collateral_details
    lca=db.query(Lca).filter(Lca.collateral_id==id).first()
    if lca is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Collateral is used in loan")
    
    db.delete(collateral)
    db.commit()
    return {"message":"Collateral deleted"}

@router.put('/collateral/update/{id}')
def updateCollateral(id:int, collateral:schema.Collateral, get_current_user:int=Depends(oauthcustomer.get_current_user), db:Session=Depends(get_db)):
    Collateral=Base.classes.collateral
    collateral_to_update=db.query(Collateral).filter(Collateral.id==id).first()
    if collateral_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Collateral not found")
    if collateral_to_update.customer_id != get_current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")
    collateral_to_update.description=collateral.description
    collateral_to_update.value=collateral.collateral_value
    db.add(collateral_to_update)
    db.commit()
    return {"message":"Collateral updated"}