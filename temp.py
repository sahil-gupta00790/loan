import smtplib
from email.message import EmailMessage

sender_email = "sahil.gupta.150520@gmail.com"
receiver_email = "sg9891@srmist.edu.in"
password = "iaxehadadmduekam"  
smtp_server = "smtp.gmail.com"  

html_file_path = './sa.html'

opt=452345

with open(html_file_path, 'r', encoding='utf-8') as file:
    html_message = file.read()


html_message = html_message.replace("{dynamic_otp}", str(opt))

email = EmailMessage()
email["From"] = sender_email
email["To"] = receiver_email
email["Subject"] = "Sent from Python!"
email.set_content(html_message, subtype="html")


smtp = smtplib.SMTP_SSL(smtp_server)
smtp.login(sender_email, password)
smtp.send_message(email)
smtp.quit()
