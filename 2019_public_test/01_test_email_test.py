# -*- coding: utf-8 -*-
# @Time : 2019/1/8 14:44 
# @Author : for 
# @File : 01_test_email_test.py 
# @Software: PyCharm
import smtplib# 创建发送邮件的实例
from email.mime.text import MIMEText # 发送的文本
#从哪里发送到发送给谁
from_addr = input('From:')
password = input('Password')
toaddr = input('To:')
#构建一个邮件发送的文本
msg = MIMEText('hello send by python')
#得到腾讯官方对外公开的api服务
smtp_server = 'smtp.qq.com'
#构造自己的实例 服务器
server = smtplib.SMTP(smtp_server,25)
#登录服务器
server.login(from_addr,password)
#发送邮件
server.sendmail(from_addr,toaddr,msg.as_string())
#关闭服务
server.close()








