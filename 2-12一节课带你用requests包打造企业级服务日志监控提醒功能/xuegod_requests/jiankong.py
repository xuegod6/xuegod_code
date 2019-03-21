import requests
import json
import sys

#--------------------------------
# 获取企业微信token
#--------------------------------


def get_token(url, corpid, corpsecret):
    token_url = '%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (url, corpid, corpsecret)
    token = requests.get(token_url).json()['access_token']
    return token

#--------------------------------
# 构建告警信息json
#--------------------------------

def messages(msg):
    values = {
        "touser":"@all",
        "msgtype":"text",
        "agentid":"1000011",
        "text":{"content":msg},
        "safe": 0
    }
    msges = (bytes(json.dumps(values),'utf-8'))
    return msges
#--------------------------------
# 发送告警信息
#--------------------------------

def send_message(url,token,data):
    send_url = '%s/cgi-bin/message/send?access_token=%s' % (url, token)
    response = requests.post(url=send_url,data=data).json()
    x = response['errcode']
    if x == 0:
        print("Successfully!")
    else:
        print("Failed!")

corpid = 'ww3cae274391cded53'
corpsecret = 'FlenqADmmSOFF72mCLZedpf-RdvBWoDMYu08Gh9sWjw'
url = 'https://qyapi.weixin.qq.com'

#函数调用

def wx_sendmsg(msg):
    test_token= get_token(url,corpid,corpsecret)
    msg_data =messages(msg)
    send_message(url,test_token,msg_data)

if __name__ == '__main__':
    msgALert=sys.argv[1]
    wx_sendmsg(msgALert)


