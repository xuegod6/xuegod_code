# -*- coding: utf-8 -*-
# @Time : 2018/12/25 13:36 
# @Author : for 
# @File : email_test.py 
# @Software: PyCharm
# import smtplib
# from email.mime.text import MIMEText
# #输入相关的内容
# from_addr = input("From:")
# #输入刚刚的QQ开启pop3 的授权码
# password = input('Password:')
# #输入发送到的QQ邮箱
# toaddr = input('To:')
# #发送内容
# msg = MIMEText('hello,send by python')
# #服务器
# smtp_server = 'smtp.qq.com'
# #创建一个SMTP实例对象，并25是默认邮件发送端口
# server = smtplib.SMTP(smtp_server,25)
# #登录SMTP服务器
# server.login(from_addr,password)
# #发送邮件 第一个参数是发送的地址，第二个是接收地址，第三个是msg然后利用as_string（）把MIMEText变成一个str，当然[toaddr] 可以写成一个列表。发送给多个人
# server.sendmail(from_addr,toaddr,msg.as_string())
# #关闭服务
# server.close()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

_user = '3403073998@qq.com'
_pwd = 'ihenvpgtjinqchbd'
_to = '3403073998@qq.com'

# 如名字所示Multipart就是分多个部分
msg=MIMEMultipart()
msg["Subject"]="don't panic"
msg["From"]=_user
msg["To"]=_to

# ---这是文字部分---
part=MIMEText("乔装打扮，不择手段")
msg.attach(part)

# ---这是附件部分---
# xlsx类型附件
# part=MIMEApplication(open('foo.xlsx', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename="foo.xlsx")
# msg.attach(part)

# jpg类型附件
part=MIMEApplication(open('text.gif', 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename="text.gif")
msg.attach(part)
s=smtplib.SMTP("smtp.qq.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
s.login(_user, _pwd)  # 登陆服务器
s.sendmail(_user, _to, msg.as_string())  # 发送邮件
s.close()
