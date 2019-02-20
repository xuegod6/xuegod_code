# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 14:46
# @Author  : for 
# @File    : 01_dingding_test.py
# @Software: PyCharm
import requests
import json
#钉钉开放平台提供的api接口
url = 'https://oapi.dingtalk.com/robot/send?access_token=a25324cafc5b0f2bb239b5e56c71e7f378f570a3d281160dbec9e4f8c4a7e493 '
#规定信息文本格式
def WriteLogByDing(content):
    headers = {
        'Content-Type':'application/json',
        'Chartset':'utf-8'
    }
    #发送的信息，json文本格式
    request_data = {
        'msgtype':'text',#发送类型格式
        #消息内容
        'text':{
            'content':content,
        },
        #
        'at':{
            #@莫个人的手机号
            'atMobiles':[],
            #控制@所有人
            'isAtAll':True
        }
    }
    #吧json文本 编程字符串格式的数据
    send_data = json.dumps(request_data)
    #这个发送的是post，请求钉钉接口
    response = requests.post(url=url,headers=headers,data=send_data)
    #返回数据
    content = response.content.decode()
    #打印返回的数据
    print(content)
if __name__ == '__main__':
    content = input('请输入你想要的信息')
    WriteLogByDing(content)