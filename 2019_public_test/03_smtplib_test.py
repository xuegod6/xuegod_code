# -*- coding: utf-8 -*-
# @Time : 2019/1/8 15:13 
# @Author : for 
# @File : 03_smtplib_test.py 
# @Software: PyCharm
import smtplib,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

user = '3403073998@qq.com'
pwd = 'ihenvpgtjinqchbd'
to = '3403073998@qq.com'
#创建一个实例 理解为一个画布
msg = MIMEMultipart()
msg['Subject'] = '这是风一般男子的测试'
msg['From'] = user
msg['To'] = to
#生出数据part 给msg天界数据
part = MIMEText('审议班的男人')
msg.attach(part)
#童谣的的道理 入股ONI发送超文本格式的文件 请一定要注意add_header给他一个文本格式
part = MIMEApplication(open('text.gif','rb').read())
part.add_header('content-disposition', 'attachment', filename='text.gif')
msg.attach(part)#给msg添加数据

try:
    #构造服务器
    s = smtplib.SMTP('smtp.qq.com',timeout=30)
    s.login(user,pwd)#登录服务器
    #发送数据内容 as_string() msg作为一个字符串
    s.sendmail(user,to,msg.as_string())

except Exception as e:
    print(e)
time.sleep(1)
s.close()#关闭服务器