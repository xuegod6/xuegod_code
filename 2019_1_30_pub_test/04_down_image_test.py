# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 10:38
# @Author  : for 
# @File    : 04_down_image_test.py
# @Software: PyCharm
import gevent
import urllib.request
from gevent import monkey
#打补丁，识别请求耗时
monkey.patch_all()
#下载图片函数
def download_image(img_url,img_name):
    try:
        print(img_url)
        #根据图盘地址打开网路进行下载
        response = urllib.request.urlopen(img_url)
        #所有的数据下载到本机指定时段文件名里面
        with open(img_name,'wb') as img_file:
            while True:
                #读取文件数据，1024个字节
                img_data = response.read(1024)
                if img_data:
                    #把数据写入到指定的文件里面
                    img_file.write(img_data)
                else:
                    #结束循环
                    break
    #有异常打印异常
    except Exception as e:
        print('图片下载异常',e)
    #没有异常打印图片下载成功
    else:
        print('图片下载成功: %s'%img_name)

if __name__ == '__main__':
    # 准备图片地址
    img_url1 = 'http://p0.so.qhmsg.com/bdr/576__/t013ee81b64eb53f6f5.jpg'
    img_url2 = "http://p2.so.qhimgs1.com/bdr/594__/t017ec94ec006189032.jpg"
    img_url3 = "http://p3.so.qhmsg.com/bdr/864__/t01f9daf42a666bb408.jpg"
    #开启协程指派响应的任务，第一个参数 对应是是个函数，第二额个对应是是函数的参数
    g1 = gevent.spawn(download_image,img_url1,'1.jpg')
    g2 = gevent.spawn(download_image,img_url2,'2.jpg')
    g3 = gevent.spawn(download_image,img_url3,'3.jpg')
#主线线程 等地啊说有的协程执行完毕之程序再推出
    gevent.joinall([g1,g2,g3])