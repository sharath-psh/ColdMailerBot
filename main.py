import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import sqlite3

# Connections
load_dotenv()
conn = sqlite3.connect('mails_db.db')

# Details
email = os.environ.get('email')
password = os.environ.get('password')
domain = input('Enter Domain:')
mailto_list = [f'hr@{domain}.com', f'recruitment@{domain}.com', f'career@{domain}.com',
               f'careers@{domain}.com', 'me@gmail.com']

subject = 'SUBJECT HERE'  # <<<EDIT
body = f'''
Hello { domain },
YOUR MAIL CONTENT HERE
'''

# DB Query


def execute_query(domain, mail, success):
    try:
        query_str = f"""INSERT INTO sentMails
                                (Domain,Mail,Success) 
                                VALUES 
                                ('{domain}','{mail}','{success}')"""
        conn.execute(query_str)
        conn.commit()
    except Exception as e:
        print('ERROR IN DB')
        print(e)


# MIME setup
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

# gmail login
try:
    s.login(email, password)
    print('Login Success')
except Exception as e:
    print('ERROR IN LOGIN:')
    print(e)

# setup MIME
message = MIMEMultipart()
message['From'] = email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# send mail
for mailto in mailto_list:
    try:
        message['To'] = mailto
        text = message.as_string()
        s.sendmail(email, mailto, text)
        print('Sent To:', mailto)
        execute_query(domain, mailto, success='True')
    except Exception as e:
        print('ERROR IN SENDING:')
        execute_query(domain, mailto, success='Fail')
        print(e)

conn.close()
s.quit()
print('====SUCCESSFULL====')
