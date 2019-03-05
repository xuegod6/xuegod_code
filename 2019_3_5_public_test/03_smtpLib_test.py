# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 15:09
# @Author  : for 
# @File    : 03_smtpLib_test.py
# @Software: PyChar
import smtplib,time
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

user = '3403073998@qq.com'
pwd = 'ihenvpgtjinqchbd'
to = '3403073998@qq.com'

msg = MIMEMultipart()
msg['Subject'] = '这个是part'
msg['From'] = user
msg['To'] = to

part = MIMEText('这是一节qq邮箱报警系统')
msg.attach(part)

part = MIMEApplication(open('2.gif','rb').read())
part.add_header('content-disposition', 'attachment', filename='2.gif')
msg.attach(part)

try:
    s = smtplib.SMTP('smtp.qq.com',timeout=30)
    s.login(user,pwd)
    s.sendmail(user,to,msg.as_string())
except Exception as e:
    print(e)

s.close()