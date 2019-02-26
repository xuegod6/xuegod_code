# -*- coding: utf-8 -*-
# @Time    : 2019/2/12 14:44
# @Author  : for 
# @File    : 01_email_test.py
# @Software: PyCharm
# user = '3403073998@qq.com'
# pwd = 'ihenvpgtjinqchbd'
# to = '3403073998@qq.com'

import smtplib
from email.mime.text import MIMEText
#发送者邮箱
from_addr = input('from:')
#pop3授权码
password = input('Password')
#邮件接受者
to_addr = input('To:')
#MIMETEXT方法构建发送的信息文本
msg = MIMEText('hello，新年快乐')
#找到腾讯服务器
smtp_server = 'smtp.qq.com'
#创建自己的服务器server
server = smtplib.SMTP(smtp_server,25)
#登录自己的服务器
server.login(from_addr,password)
#利用自己的服务器发送邮件，第一参数发送者，二个接受者，第三个参数是发送的信息
server.sendmail(from_addr,to_addr,msg.as_string())
#关闭自己的服务器
server.close()





