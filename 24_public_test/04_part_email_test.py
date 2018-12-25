# -*- coding: utf-8 -*-
# @Time : 2018/12/25 15:12 
# @Author : for 
# @File : 04_part_email_test.py 
# @Software: PyCharm
import smtplib,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

user = '3403073998@qq.com'
pwd = 'ihenvpgtjinqchbd'
to = '3403073998@qq.com'

msg = MIMEMultipart()

msg['Subject'] ='这是风一般男子的测试'
msg['From'] = user
msg['To'] = to
part = MIMEText('<html><body><h1>你好</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>','html','utf-8')
msg.attach(part)

part = MIMEApplication(open('1.png','rb').read())
part.add_header('content-disposition', 'attachment',filename='1.png')
msg.attach(part)

part = MIMEApplication(open('0.png','rb').read())
part.add_header('content-disposition', 'attachment',filename='0.png')
msg.attach(part)

try:
    s = smtplib.SMTP('smtp.qq.com',timeout=30)
    s.login(user,pwd)

    s.sendmail(user,to,msg.as_string())

except Exception as e:
    print(e)

time.sleep(2)

s.close()