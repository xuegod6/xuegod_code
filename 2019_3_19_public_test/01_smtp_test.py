# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 10:15
# @Author  : for 
# @File    : 01_smtp_test.py
# @Software: PyCharm
user = '3403073998@qq.com'
pwd = 'ihenvpgtjinqchbd'
to = '3403073998@qq.com'

from email.mime.text import MIMEText
#todo : 构造自己的发送者 接受者 pop3 授权码
from_addr = input('from:')
password = input('Password:')
to_addr = input('To:')
#todo ： 发送的文本
msg = MIMEText('hello send by python 大家爱好 我是for')
#todo: 构造自急的服务器
import smtplib
smtp_server = 'smtp.qq.com'
#25端口 不限流
server = smtplib.SMTP(smtp_server,25)
#登录服务器
server.login(from_addr,password)
#发送邮件信息第一个参数发送者，第二个参数接受者，的三个参数是发送的文本
server.sendmail(from_addr,to_addr,msg.as_string())
#关闭自己的服务器
server.close()
