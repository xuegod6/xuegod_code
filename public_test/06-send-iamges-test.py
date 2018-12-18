# -*- coding: utf-8 -*-
# @Time : 2018/12/10 15:17 
# @Author : for 
# @File : 06-send-iamges-test.py 
# @Software: PyCharm
import smtplib,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

user = '3403073998@qq.com'
pwd = 'ihenvpgtjinqchbd'
to = '3403073998@qq.com'
# 创建实力对象 相当于一个画布
msg = MIMEMultipart()
#设置主题
msg['Subject'] = '风一般的男子的测试'
msg['From'] = user
msg['To'] = to
#part想党头发 一块一块的
part = MIMEText('神一般的男人')
#画布上执行
msg.attach(part)
#得到附件内容得到图片文件的所有数据
part = MIMEApplication(open('1.png','rb').read())
part.add_header('content-disposition', 'attachment',
               filename='1.png')
msg.attach(part)

try:
    s = smtplib.SMTP('smtp.qq.com',timeout=30)
    s.login(user,pwd)
    s.sendmail(user,to,msg.as_string())
except Exception as e:
    print(e)
time.sleep(2)

s.close()