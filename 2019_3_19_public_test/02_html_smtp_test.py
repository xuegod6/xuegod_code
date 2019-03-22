# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 10:27
# @Author  : for 
# @File    : 02_html_smtp_test.py
# @Software: PyCharm
from email.mime.text import MIMEText
#构造自己的发送者
from_addr = '3403073998@qq.com'
password = 'ihenvpgtjinqchbd'
toaddr = '3403073998@qq.com'
#发送的文本内容第一个是字符串，第二个是格式 的三个字符集
msg = MIMEText('<html><body><h1>你好</h1>' +
               '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
               '</body></html>','html','utf-8'
               )
#邮件主题 发送者 接受者
msg['Subject'] = '这是一个而文件的测试'
msg['From'] = from_addr
msg['To'] = toaddr
#todo: 构造自己的发送邮箱服务器
import smtplib
#自己的服务器
server = smtplib.SMTP('smtp.qq.com',25)
#登录自己的服务器
server.login(from_addr,password)
#发送email 第一个参数 发宋哲 第二个 接受者 第三个 发哦发送的文本内容
server.sendmail(from_addr,toaddr,msg.as_string())
#关闭自己的服务器
server.close()

