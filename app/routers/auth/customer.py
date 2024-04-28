import numbers
from fastapi import APIRouter ,Depends , status ,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db , Base
from . import email
from app import oauthcustomer, utils , schema

router=APIRouter(
    tags=['Authentication:customer']
)


@router.get('/signup/customer')
def signup(email_id:schema.GetEmail,db:Session=Depends(get_db)):
    Customer=Base.classes.customer_login
    customer=db.query(Customer).filter(email_id.email==Customer.email).first()
    if customer is not None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email already exists")
    otp=email.sendEmail(email_id.email)
    return {"otp":otp}

@router.post('/add/customer',response_model=schema.UserOut, status_code=status.HTTP_201_CREATED)
def addUser(user_credential:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    Login=Base.classes.customer_login
    password=utils.hash(user_credential.password)
    userLogin=Login(email=user_credential.username, password=password)
    db.add(userLogin)
    db.flush()
    db.commit()
    return userLogin

@router.get('/login/customer')
def addEmployee(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    Customer=Base.classes.customer_login
    customer=db.query(Customer).filter(user_credentials.username==Customer.email).first()
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Customer not found")
    if not utils.verify(user_credentials.password,customer.password):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid password")
    
    access_token=oauthcustomer.create_access_token(data={"user_id":customer.id})


    return{ "access_token":access_token , "token_type":"bearer"}

@router.post('/details/customer')
def get_employee_details(details:schema.Customer_details,dbLSession=Depends(get_db),get_current_user:int=Depends(oauthcustomer.get_current_user)):
    
    Customer=Base.classes.customer_information
    Phone_number=Base.classes.phone_number 
    customer=Customer(id=get_current_user,name=details.name,  address=details.address,pan_number =details.pan_card, aadhaar_number=details.aadhaar_card, income=details.income, employment_type=details.employment_type)
    dbLSession.add(customer)
    dbLSession.flush()
    dbLSession.commit()
    phone_number=Phone_number(customer_id=get_current_user, phone_number=details.phone_number)
    dbLSession.add(phone_number)
    dbLSession.flush()
    dbLSession.commit()
    
    return customer




