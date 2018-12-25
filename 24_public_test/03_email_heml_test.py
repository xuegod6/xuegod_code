# -*- coding: utf-8 -*-
# @Time : 2018/12/25 14:54 
# @Author : for 
# @File : 03_email_heml_test.py 
# @Software: PyCharm
from email.mime.text import MIMEText
user = '3403073998@qq.com'
pwd = 'ihenvpgtjinqchbd'
to = '3403073998@qq.com'

#构造发送者以及密码接受者
from_addr = input('from:')
password = input('password:')
to_addr  = input('to_addr:')
#构建发送的信息
msg = MIMEText('<html><body><h1>你好</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>','html','utf-8'
)
#规定邮件的主题
msg['Subject'] = '这是风一般男子的邮件测试'
msg['From'] = from_addr
msg['To'] = to_addr

smtp_server ='smtp.qq.com'
import smtplib
#服务器示例
server = smtplib.SMTP(smtp_server,25)
#登录服务器
server.login(from_addr,password)
#发送信息
server.sendmail(from_addr,to_addr,msg.as_string())
#关闭服务器
server.close()






