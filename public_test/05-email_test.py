# -*- coding: utf-8 -*-
# @Time : 2018/12/10 15:00 
# @Author : for 
# @File : 05-email_test.py 
# @Software: PyCharm
from email.mime.text import MIMEText
#发送邮件 发送者接受者
from_addr = input('Form:')
password = input('Passeord')
toaddr = input('To:')
#发送的内容个，规定上交文本的格式，字符的格式
msg = MIMEText('<html><body><h1>你好</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>','html','utf-8')
#设置主题
msg['Subject'] = '这是风一般男人的邮件'
#设置发送者
msg['From'] = from_addr
#接受者
msg['to'] = toaddr
import smtplib
#创建smtp这个服务器，qq地外发放到服务，25
server = smtplib.SMTP('smtp.qq.com',25)
#登录服务器
server.login(from_addr,password)
#发送邮箱
server.sendmail(from_addr,toaddr,msg.as_string())
#关闭服务
server.close()
