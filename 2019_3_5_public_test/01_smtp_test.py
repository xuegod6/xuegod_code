# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 14:44
# @Author  : for 
# @File    : 01_smtp_test.py
# @Software: PyCharm
# user = '3403073998@qq.com'
# pwd = 'ihenvpgtjinqchbd'
# to = '3403073998@qq.com'
import smtplib
from email.mime.text import MIMEText
#构造发送者接受者 注意pass是pop3s授权码
from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
#构造发送邮件的信息正文文本
msg = MIMEText('hello send by python ')
#腾讯对公的 接口
smtp_server = 'smtp.qq.com'
#构造自己的邮箱
server = smtplib.SMTP(smtp_server,25)
#登录自己的邮箱
server.login(from_addr,password)
#发送邮件
server.sendmail(from_addr,to_addr,msg.as_string())
#关闭自己的邮箱
server.close()













