# -*- coding: utf-8 -*-
# @Time : 2018/12/25 14:42 
# @Author : for 
# @File : 02_emiail_test.py 
# @Software: PyCharm
# user = '3403073998@qq.com'
# pwd = 'ihenvpgtjinqchbd'
# to = '3403073998@qq.com'

import smtplib
from email.mime.text import MIMEText
#g构造发送人就收人
from_addr = input('from:')
password = input('Password:')
to_addr = input('To')
#构造发送的消息
mag = MIMEText('hello,send by python')
#腾讯服务
smtp_server = 'smtp.qq.com'
#一个服务器实力并且以端口为25 发
server = smtplib.SMTP(smtp_server,25)
#登录
server.login(from_addr,password)
#发送邮件
server.sendmail(from_addr,to_addr,mag.as_string())
#关闭服务器
server.close()



