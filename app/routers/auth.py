from fastapi import APIRouter ,Depends , status ,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db , Base
from .. import utils , oauth
from .. import schema
from fastapi_mail import fastmail, MessageSchema, ConnectionConfig , FastMail
import smtplib
from email.message import EmailMessage
import secrets
from app.config import settings


router=APIRouter(tags=['Authentication'])


@router.post('/login/user')
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    login=Base.classes.customer_login
    user=db.query(login).filter(login.email==user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    access_token=oauth.create_access_token(data={"user_id":user.id})

    return {"access_token":access_token, "token_type":"bearer"}


       


@router.post('/signup/user',response_model=schema.UserOut)
def signup(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    login=Base.classes.customer_login
    password=utils.hash(user_credentials.password)
    user=login(email=user_credentials.username, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    

    return user



@router.post('/login/employee')
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    login=Base.classes.customer_login
    user=db.query(login).filter(login.email==user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    access_token=oauth.create_access_token(data={"user_id":user.id})

    return {"access_token":access_token, "token_type":"bearer"}

@router.post('/signup/employee')
def signup(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    login=Base.classes.customer_login
    a=sendEmail(user_credentials.username)

    #password=utils.hash(user_credentials.password)
    #user=login(email=user_credentials.username, password=password)
    #db.add(user)
    #db.commit()
    #db.refresh(user)
    

    return {"id":a}


def sendEmail(a:str):
    sender_email = str(settings.email)
    receiver_email = a
    password = settings.email_password
    smtp_server = "smtp.gmail.com"  

    html_file_path = "./sa.html"

    otp=secrets.randbelow(899999-1)+100000

    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_message = file.read()


    html_message = html_message.replace("{dynamic_otp}", str(otp))

    email = EmailMessage()
    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = "Sent from Python!"
    email.set_content(html_message, subtype="html")


    smtp = smtplib.SMTP_SSL(smtp_server)
    smtp.login(sender_email, password)
    smtp.send_message(email)
    smtp.quit()

    return otp

    
