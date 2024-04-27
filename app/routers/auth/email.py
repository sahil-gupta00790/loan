from email.message import EmailMessage
import smtplib
from app.config import settings
import secrets


def sendEmail(a:str):
    sender_email = str(settings.email)
    receiver_email = a
    password = settings.email_password
    smtp_server = "smtp.gmail.com"  

    html_file_path = 'C:/Users/Sahil/Codes/Python-APIS/Loan_management_apis/app/routers/sa.html'

    otp=secrets.randbelow(899999-1)+100000

    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_message = file.read()


    html_message = html_message.replace("{dynamic_otp}", str(otp))

    email = EmailMessage()
    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = "Email Verification"
    email.set_content(html_message, subtype="html")

    
    smtp = smtplib.SMTP_SSL(smtp_server)
    smtp.login(sender_email, password)
    smtp.send_message(email)
    smtp.quit()


    return otp
