# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 15:04
# @Author  : for 
# @File    : 02_dingding_link_test.py
# @Software: PyCharm
import requests
import json
url = 'https://oapi.dingtalk.com/robot/send?access_token=a25324cafc5b0f2bb239b5e56c71e7f378f570a3d281160dbec9e4f8c4a7e493 '
headers = {
    'Content-Type':'application/json',
    'Chartset':'utf-8'
}
#发送的信息，json文本格式
request_data = {
    "feedCard": {
        "links": [
            {
                "title": "时代的火车向前开",
                "messageURL": "https://mp.weixin.qq.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI",
                "picURL": "https://www.dingtalk.com/"
            },
            {
                "title": "时代的火车向前开2",
                "messageURL": "https://mp.weixin.qq.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI",
                "picURL": "https://www.dingtalk.com/"
            }
        ]
    },
    "msgtype": "feedCard"
}



#吧json文本 编程字符串格式的数据
send_data = json.dumps(request_data)
#这个发送的是post，请求钉钉接口
response = requests.post(url=url,headers=headers,data=send_data)
#返回数据
content = response.content.decode()
#打印返回的数据
print(content)