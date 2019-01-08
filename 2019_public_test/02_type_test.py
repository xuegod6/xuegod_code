# -*- coding: utf-8 -*-
# @Time : 2019/1/8 14:57 
# @Author : for 
# @File : 02_type_test.py 
# @Software: PyCharm
from email.mime.text import MIMEText#x必要发搜个文本的方法
#构造发件人收件人
form_addr = '3403073998@qq.com'

passwrod = 'ihenvpgtjinqchbd'

toaddr = '3403073998@qq.com'
#构造发送的信息对应的文本格式
msg = MIMEText('<html><body><h1>你好</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>','html','utf-8'
)
#构造发送者接受者的主题
msg['Subject'] = '这是风衣班男子的测试'
msg['From'] = form_addr
msg['To'] = toaddr
#构造服务器
smtp_server = 'smtp.qq.com'#腾讯对公规定免费接口

import smtplib
#创建实例 自己服务器
server = smtplib.SMTP(smtp_server,25)
#登录服务器
server.login(form_addr,passwrod)
#利用登录号的服务器 发送邮件
server.sendmail(form_addr,toaddr,msg.as_string())
#关闭服务
server.close()
