# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 21:52
# @Author  : for 
# @File    : 07_spider_image_test.py
# @Software: PyCharm
import gevent,requests#pip install requests
from gevent import monkey
from urllib import request
#打补丁，识别网路延迟
monkey.patch_all()
#下载图片
def download_img(num):
    #开启下载
    print('start download')
    #图片的url地址
    url = 'http://image.so.com/zj?ch=beauty&sn=150&listtype=new&temp=1'
    #模拟浏览器
    headers={
        'Referer': 'http://image.so.com/z?ch=beauty',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    #模拟浏览器访问服务器发送内容
    str_data = '''h: beauty
    sn: 30
    listtype: new
    temp: 1'''

    #简单的数据清洗
    send_data = {}
    #进行一行分割
    for data in str_data.splitlines():
        line_data = data.split(': ')#返回一个列表
        if len(line_data) == 2:#如果这个列表当中有两个数据
            key,value = line_data# a,b = [1,2] #进行序列解包赋值！
            if key and value:#如果两者key和 value都有值 我就进行 搭建send_data
                send_data[key] = value
    #end_data = {'h':'beauty','sn':'30'}
    send_data['sn'] = eval(str(num)+'*'+'30') #eval（'3 * 4'）#z字典的修改
    #requests 这个方法进行网略请求，模拟刘燃气访问服务器返回结果
    response = requests.get(url,headers=headers,params=send_data)
    #json()方法 转换为python可操作对象{‘a" ;1}
    json_data = response.json()['list']
    #利用么酷的方法，序列解包赋值
    for index,src in enumerate(json_data):
        #获取图片url地址
        image_url = src['qhimg_url']
        try:
            #给定本地图片地址
            image_name = './360_image/'+image_url[-8:]
            #吧网路上的图片下载到本地
            request.urlretrieve(url=image_url,filename=image_name)
        except Exception as e:
            print(e)
        else:
            #format格式化
            print('{} is download'.format(image_name))
        print('image is download')

if __name__ == '__main__':
    num = int(input('你想要爬取的图片的组:'))
    #列表推导式完成协程任务分发
    gevent.joinall([gevent.spawn(download_img,i)for i in range(1,num+1)])