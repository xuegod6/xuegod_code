# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 10:41
# @Author  : for 
# @File    : 03_image_smtp_test.py
# @Software: PyCharm

import smtplib,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

user = 'for'
pwd = 'ihenvpgtjinqchbd'
to = '3403073998@qq.com'
# 相当于 创建一个额邮件画布
msg = MIMEMultipart()
#字啊画布上 换行主题
msg['Subject'] = '这是主题'
msg['From'] = user
msg['To'] = to
#回不上 画上文本
part = MIMEText('这是我发送的正文文本')
msg.attach(part)#利用这个方法获取文本

#发送附件 画布上画上附件
part = MIMEApplication(open('2.jpg','rb').read())
#给数据佳航头部信息 让浏览器了解咱们发送的数据格式
part.add_header('content-disposition', 'attachment', filename='2.jpg')
msg.attach(part)
#todo 构造自己的邮箱服务器
try:

    s = smtplib.SMTP('smtp.qq.com',timeout=30)
    s.login(user,pwd)
    s.sendmail(user,to,msg.as_string())

except Exception as e:
    print(e)

finally:
    s.close()



