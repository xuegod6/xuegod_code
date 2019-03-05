# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 14:59
# @Author  : for 
# @File    : 02_email_test.py
# @Software: PyCharm

from email.mime.text import MIMEText

from_addr = '3403073998@qq.com'
password = 'ihenvpgtjinqchbd'
toaddr = '3403073998@qq.com'

msg = MIMEText('<html><body><h1>你好</h1>' +
               '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
               '</body></html>','html','utf-8'
               )

msg['Subject'] = '这是一个邮件的测试'
msg['From'] = from_addr
msg['To'] = toaddr

import smtplib

smtp_server = 'smtp.qq.com'

server = smtplib.SMTP(smtp_server,25)

server.login(from_addr,password)

server.sendmail(from_addr,toaddr,msg.as_string())

server.close()

