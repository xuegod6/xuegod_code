# -*- coding: utf-8 -*-
# @Time : 2018/12/10 13:31 
# @Author : for 
# @File : 03-email-test.py 
# @Software: PyCharm
from email.mime.text import MIMEText
from_addr = input("From:")

password = input('Password:')

toaddr = input('To:')

msg = MIMEText('<html><body><h1>你好</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
#设置标题一些主题，邮件来自，和邮件发送
msg['Subject'] = '这是风一般的男人的邮件'
msg['From'] = from_addr
msg['To'] = toaddr
smtp_server = 'smtp.qq.com'

import smtplib
#创建一个SMTP实例对象，并25是默认邮件发送端口
server = smtplib.SMTP(smtp_server,25)
#登录SMTP服务器
server.login(from_addr,password)
#发送邮件 第一个参数是发送的地址，第二个是接收地址，第三个是msg然后利用as_string（）把MIMEText变成一个str，当然[toaddr] 可以写成一个列表。发送给多个人
server.sendmail(from_addr,toaddr,msg.as_string())
server.close()

