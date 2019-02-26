# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 21:23
# @Author  : for 
# @File    : 06_gevent_shizahn_test.py
# @Software: PyCharm
import gevent
import urllib.request #网略强求模块
from gevent import monkey
#打补丁
monkey.patch_all()
#生成函数下载图片
def download_img(img_url,img_name):
    try:
        print(img_url)#打印url地址
        #模拟浏览器返回得到数据
        response = urllib.request.urlopen(img_url)
        #打开本地文件
        with open(img_name,'wb') as img_file:

            while True:
                #写入网路响应的数据
                img_data = response.read(1024)
                if img_data:
                    img_file.write(img_data)
                else:
                    break
    except Exception as e:
        print('图片下载异常:',e)
    else:
        print('图片下载成功:%s'%img_name)

if __name__ == '__main__':
    # 准备图片地址
    img_url1 = 'http://p0.so.qhmsg.com/bdr/576__/t013ee81b64eb53f6f5.jpg'
    img_url2 = "http://p2.so.qhimgs1.com/bdr/594__/t017ec94ec006189032.jpg"
    img_url3 = "http://p3.so.qhmsg.com/bdr/864__/t01f9daf42a666bb408.jpg"
    #创建协程分布任务
    g1 = gevent.spawn(download_img,img_url1,'1.jpg')
    g2 = gevent.spawn(download_img,img_url2,'2.jpg')
    g3 = gevent.spawn(download_img,img_url3,'3.jpg')
    #阻塞获取所有数据
    gevent.joinall([g1,g2,g3])
