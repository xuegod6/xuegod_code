# -*- coding: utf-8 -*-
# @Time : 2018/12/10 14:45 
# @Author : for 
# @File : 04-send_emain.py 
# @Software: PyCharm
import smtplib
from email.mime.text import MIMEText
#规定发送
from_addr = input('From')
#password授权码 pop3
password = input('Password')
#某个邮箱
toaddr = input('To:')
#发送内容
mag = MIMEText('hello,send by python')
#服务器
smtp_server = 'smtp.qq.com'
#厂家爱你一个smtp实例对象，25端口发送
server = smtplib.SMTP(smtp_server,25)
#登录smtp服务器
server.login(from_addr,password)
#发送邮件，发哦送的内容成str
server.sendmail(from_addr,toaddr,mag.as_string())
#关闭
server.close()




