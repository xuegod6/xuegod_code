# -*- coding: utf-8 -*-
# @Time : 2019/1/23 10:41 
# @Author : for 
# @File : 03_part_test.py 
# @Software: PyCharm
import smtplib,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
#构造发送这 接受者
user = '3403073998@qq.com'
pwd = 'ihenvpgtjinqchbd'
to = '3403073998@qq.com'
#创建一个实例，想想成一个画布
msg= MIMEMultipart()
#画布上添加主题，发送者 接受者
msg['Subject'] = '这是一个附件的测试'
msg['From'] = user
msg['To'] = to
#画布上画上正文内容
part = MIMEText('这是一个文本内容')
msg.attach(part)
#添加附件
part = MIMEApplication(open('1.mp4','rb').read())
#邮箱明白我们发哦送的数据是什么格式
part.add_header('content-disposition', 'attachment', filename='1.mp4')
msg.attach(part)
#构造自己服务器并且发送
try:
    s = smtplib.SMTP('smtp.qq.com',timeout=30)
    s.login(user,pwd)
    s.sendmail(user,to,msg.as_string())
except Exception as e:
    print(e)
time.sleep(2)
#关闭服务器
s.close()



