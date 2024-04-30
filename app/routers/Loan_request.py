from typing import List
from fastapi import APIRouter ,Depends , status ,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db , Base
from app import oauthcustomer, utils , schema
from app.schema import Loan

router=APIRouter(
    tags=['Loan']
    )

@router.post('/loan/request')
def create_loan(loan:schema.Loan,get_current_user:int=Depends(oauthcustomer.get_current_user), db:Session=Depends(get_db),collateral_id: int = None ):
    
    Loan=Base.classes.loan
    new_loan_request=Loan(loan_amount=loan.loan_amount, loan_type=loan.loan_type, loan_term=loan.loan_term, loan_interest=loan.loan_interest , repayment_frequency=loan.repayment_frequency )
    db.add(new_loan_request)
    db.commit()
    db.refresh(new_loan_request)

    lca=Base.classes.loan_customer_officer_collateral_details
    new_req=lca(customer_id=get_current_user, loan_id=new_loan_request.id, collateral_id=collateral_id)
    db.add(new_req)
    db.commit()
    db.refresh(new_req)


    return {"message":"Loan request created successfully"}


@router.get('/loan/status/',response_model=List[schema.Loan_status])
def checkstatus(get_current_user:int=Depends(oauthcustomer.get_current_user), db:Session=Depends(get_db)):
    Loan=Base.classes.loan_customer_officer_collateral_details
    loan=db.query(Loan).filter(Loan.customer_id==get_current_user).all()
    if loan is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Loan not found")
    loan_ids = [loan.loan_id for loan in loan]
    Loan=Base.classes.loan

    loan_details=db.query(Loan).filter(Loan.id.in_(loan_ids)).all()
    
    return loan_details


@router.get('/loan/status/{id}')
def checkstatus(id:int,get_current_user:int=Depends(oauthcustomer.get_current_user), db:Session=Depends(get_db)):
    Loan=Base.classes.loan_customer_officer_collateral_details
    loan=db.query(Loan).filter(Loan.customer_id==get_current_user, Loan.loan_id==id).first()
    if loan is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Loan not found")
    Loan=Base.classes.loan
    loan_details=db.query(Loan).filter(Loan.id==id).first()
    return loan_details


@router.delete('/loan/delete/{id}')
def delete_loan(id:int, get_current_user:int=Depends(oauthcustomer.get_current_user), db:Session=Depends(get_db)):
    Loan=Base.classes.loan_customer_officer_collateral_details
    loan=db.query(Loan).filter(Loan.customer_id==get_current_user, Loan.loan_id==id).first()
    if loan is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Loan not found")
    Loan=Base.classes.loan
    loan_details=db.query(Loan).filter(Loan.id==id).first()
    if loan_details.approval_status=="True":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Loan is approved,money is already credited into account.Cannot be cancelled now")
    
    db.delete(loan)
    db.commit()
    db.delete(loan_details)
    db.commit()

    return {"message":"Loan deleted successfully"}

@router.post('/loan/edit/{id}')
def edit_loan(id:int, loan:schema.Loan, get_current_user:int=Depends(oauthcustomer.get_current_user), db:Session=Depends(get_db)):
    Loan=Base.classes.loan_customer_officer_collateral_details
    loan_details=db.query(Loan).filter(Loan.customer_id==get_current_user, Loan.loan_id==id).first()
    if loan_details is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Loan not found")
    Loan=Base.classes.loan
    loan_details=db.query(Loan).filter(Loan.id==id).first()
    if loan_details.approval_status=="True":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Loan is approved, cannot edit now")

    loan_details.loan_amount=loan.loan_amount
    loan_details.loan_type=loan
    loan_details.loan_term=loan.loan_term
    loan_details.repayment_frequency=loan.repayment_frequency
    db.add(loan_details)
    db.commit()
    db.refresh(loan_details)

    return loan_details

