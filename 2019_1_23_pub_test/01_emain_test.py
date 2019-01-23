# -*- coding: utf-8 -*-
# @Time : 2019/1/23 10:12 
# @Author : for 
# @File : 01_emain_test.py 
# @Software: PyCharm
import smtplib#构建发送规定服务器模块
from email.mime.text import MIMEText#发送的文本内容
#构造发送者 和接受者，pop3的数千吗
from_addr = input('From:')
password = input('Password:')
to_addr = input('To')
#构造发送的信息
msg = MIMEText('hello ,honeyhong')
#腾讯对公借口
smtp_server = 'smtp.qq.com'
#构造自己的有建发送的服务器
server = smtplib.SMTP(smtp_server,25)
#登录服务器
server.login(from_addr,password)
#发送邮件，第一个参数发哦送这，第二个参数接受者，第三个参数发送的信息
server.sendmail(from_addr,to_addr,msg.as_string())
#关闭服务器
server.close()

