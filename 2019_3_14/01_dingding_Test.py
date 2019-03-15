# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 10:10
# @Author  : for 
# @File    : 01_dingding_Test.py
# @Software: PyCharm
import requests
import json
url = 'https://oapi.dingtalk.com/robot/send?access_token=a25324cafc5b0f2bb239b5e56c71e7f378f570a3d281160dbec9e4f8c4a7e493'


headers = {
    'Content-Type':'application/json',
    'Chartset':'utf-8'
}
request_data = {
    "actionCard": {
        "title": "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
        "text": "![screenshot](@lADOpwk3K80C0M0FoA) \n\n #### 乔布斯 20 年前想打造的苹果咖啡厅 \n\n Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划",
        "hideAvatar": "0",
        "btnOrientation": "0",
        "btns": [
            {
                "title": "内容不错",
                "actionURL": "https://www.dingtalk.com/"
            },
            {
                "title": "不感兴趣",
                "actionURL": "https://www.dingtalk.com/"
            }
        ]
    },
    "msgtype": "actionCard"
}
#todo:把数据编程json文本格式的字符串
send_data = json.dumps(request_data)
#todo:发送网络请求
response = requests.post(url=url,headers=headers,data=send_data)
#todo 接受返回的结果 response.json()
content = response.content.decode()
print(content)



