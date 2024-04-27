import numbers
from fastapi import APIRouter ,Depends , status ,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db , Base
from . import email
from app import oauthemployee, utils , schema

router=APIRouter(
    tags=['Authentication:officer']
)


@router.get('/signup/employee')
def signup(email_id:schema.GetEmail,db:Session=Depends(get_db)):
    Employee=Base.classes.employee_login
    employee=db.query(Employee).filter(email_id.email==Employee.email).first()
    if employee is not None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email already exists")
    otp=email.sendEmail(email_id.email)
    return {"otp":otp}

@router.post('/add/employee',response_model=schema.UserOut, status_code=status.HTTP_201_CREATED)
def addUser(user_credential:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    Login=Base.classes.employee_login
    password=utils.hash(user_credential.password)
    userLogin=Login(email=user_credential.username, password=password)
    db.add(userLogin)
    db.flush()
    db.commit()
    return userLogin

@router.get('/login/employee')
def addEmployee(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    Employee=Base.classes.employee_login
    employee=db.query(Employee).filter(user_credentials.username==Employee.email).first()
    if employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Employee not found")
    if not utils.verify(user_credentials.password,employee.password):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid password")
    
    access_token=oauthemployee.create_access_token(data={"user_id":employee.id})


    return{ "access_token":access_token , "token_type":"bearer"}

@router.post('/details/employee')
def get_employee_details(details:schema.Officer_details,dbLSession=Depends(get_db),get_current_user:int=Depends(oauthemployee.get_current_user)):
    
    

    Employee=Base.classes.employee_details
    employee=Employee(id=get_current_user,Name=details.name, phone_number=details.phone_number, address=details.address,pan_number =details.pan_card, aadhaar_number=details.aadhaar_card, Salary=details.Salary, designation=details.designation)
    dbLSession.add(employee)
    dbLSession.flush()
    dbLSession.commit()
    return employee





