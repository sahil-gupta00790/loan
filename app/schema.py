from pydantic import BaseModel, EmailStr, condecimal 
from datetime import datetime
from pydantic import BaseModel, Field
from decimal import Decimal

from sqlalchemy import NUMERIC, Numeric

class TokenData(BaseModel):
    id:str=None


class UserOut(BaseModel):
    id:int
    email:str
    created_at:datetime
    class Config:
        orm_mode=True

class GetEmail(BaseModel):
    email:EmailStr




# Define the schema class for officer details
class Officer_details(BaseModel):
    id:int=None
    name: str
    pan_card: str
    aadhaar_card: Decimal = Field( gt=Decimal('0'), le=Decimal('999999999999'))  # Aadhaar number is a 12-digit number
    address: str
    Salary: Decimal = Field( gt=Decimal('0'))  # Salary can be a positive Decimal
    designation: str
    phone_number: Decimal = Field( le=Decimal('9999999999'))  # Phone number is a 10-digit number

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Customer_details(BaseModel):
    id:int=None
    name: str
    pan_card: str
    aadhaar_card: Decimal = Field(gt=Decimal('0'), le=Decimal('999999999999')) 
    address: str
    income: Decimal = Field( gt=Decimal('0')) 
    employment_type:str
    phone_number: Decimal = Field( le=Decimal('9999999999'))
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Loan(BaseModel):
    id: int = None
    loan_amount: Decimal = Field(..., gt=Decimal('0'))
    loan_type: str
    loan_interest: Decimal = Field(..., gt=Decimal('0'))
    loan_term: int
    repayment_frequency: int = Field(..., gt=0)

    

    class Config:
        orm_mode = True

class Collateral(BaseModel):
    id:int=None
    description:str
    collateral_value:Decimal=Field(...,gt=Decimal('0'))
    #customer_id:int

    class Config:
        orm_mode = True

class Loan_status(BaseModel):
    id:int
    approval_status:bool
    loan_amount:Decimal 
    loan_interest:Decimal 
    loan_term:int
    repayment_frequency:int 
    class Config:
        orm_mode = True
