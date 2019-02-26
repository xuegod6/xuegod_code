# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 16:30
# @Author  : for 
# @File    : 03_shizhan_test.py
import json
import requests
url= 'https://oapi.dingtalk.com/robot/send?access_token=a25324cafc5b0f2bb239b5e56c71e7f378f570a3d281160dbec9e4f8c4a7e493'
headers = {
    "Content-Type": "application/json",
    "Chartset": "utf-8"
}

request_data = {
    "msgtype": "text",
    "text": {
        "content": "哈哈哈哈"
    },
    "at": {
        "atMobiles": [],
        "isAtAll": True
    }
}

sendData = json.dumps(request_data)
response = requests.post(url = url,headers = headers,data = sendData)
content = response.content.decode()
print(content)

