from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from matplotlib.pyplot import text


def send_email(to_addr,subject,message):
    from_addr="arifurfi.arif6@gmail.com"
    msg=MIMEMultipart()
    msg["From"]=from_addr
    msg["To"]=to_addr
    msg["subject"]=subject
    
    body=message

    msg.attach(MIMEText(body,'plain'))

    smtp_server=SMTP('smtp.gmail.com',587
    )

    

    smtp_server.ehlo()

    smtp_server.starttls()
    try:


        smtp_server.login(from_addr,"8765881360")
        
        text=msg.as_string()

        smtp_server.sendmail(from_addr,to_addr,text)


    except:
        print("Error occured while sending the mail")
    
    finally:

        smtp_server.quit()