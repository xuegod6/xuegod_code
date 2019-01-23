# -*- coding: utf-8 -*-
# @Time : 2019/1/23 10:25 
# @Author : for 
# @File : 02_email_html_test.py 
# @Software: PyCharm
from email.mime.text import MIMEText
#构造发送者接受者密码
from_addr = '3403073998@qq.com'
password = 'ihenvpgtjinqchbd'
to_addr = '3403073998@qq.com'
#构造发送的文本内容，第一个是内容，文本格式，文本字符集
msg = MIMEText('<html><body><h1>你好</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8'
)
#主题
msg['Subject'] = '这是一个邮件的测试'
#发送者
msg['From'] = from_addr
#接受者
msg['To'] = to_addr
#腾讯对公借口
smtp_server = 'smtp.qq.com'

import smtplib
#构造自己的服务器
server = smtplib.SMTP(smtp_server,25)
#登录服务
server.login(from_addr,password)
#发送邮件
server.sendmail(from_addr,to_addr,msg.as_string())
#关闭服务
server.close()






