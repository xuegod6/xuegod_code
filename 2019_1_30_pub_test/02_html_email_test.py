import requests
import json
url = 'https://oapi.dingtalk.com/robot/send?access_token=a25324cafc5b0f2bb239b5e56c71e7f378f570a3d281160dbec9e4f8c4a7e493  '

headers = {
    "Content-Type": "application/json",
    "Chartset": "utf-8"
}
#要发送的文本是json格式
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
#把json转变为字符串格式数据
send_data = json.dumps(request_data)
#这个是发送post请求，请求钉钉接口
response = requests.post(url=url,headers=headers,data=send_data)
#讲求成功后返回的数据
content = response.content.decode()
#打印
# 课程 vip 标准
# 替换 视频
print(content)

# import sys
# import json
# import requests
# url = 'https://oapi.dingtalk.com/robot/send?access_token=a25324cafc5b0f2bb239b5e56c71e7f378f570a3d281160dbec9e4f8c4a7e493  '
# def WriteLogByDing(content):
#     headers = {
#         "Content-Type": "application/json",
#         "Chartset": "utf-8"
#     }
#
#     request_data = {
#         "msgtype": "text",
#         "text": {
#             "content": content
#         },
#         "at": {
#             "atMobiles": [],
#             "isAtAll": True
#         }
#     }
#
#     sendData = json.dumps(request_data)
#     response = requests.post(url = url,headers = headers,data = sendData)
#     content = response.content.decode()
#     print(content)
#
# if __name__ == "__main__":
#     content = input('请输入想要的信息')
#     # content = sys.argv[1]
#     WriteLogByDing(content)
