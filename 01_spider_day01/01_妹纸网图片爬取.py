# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 9:43
# @Author  : for 
# @File    : 01_妹纸网图片爬取.py
# @Software: PyCharm
import os
import re
import time
import requests
from urllib import request
url = 'http://www.meizitu.com/a/pure_{}.html'
from fake_useragent import UserAgent
headers  ={
    'User-Agent':UserAgent().random
}
all_url = []
#todo:提取网站的url地址
class MeiZhi():
    def __init__(self):
        self.url = url
        self.headers = {
            'User-Agent':UserAgent().random
        }
    def html_url(self,run_num,end_num):
        for i in range(run_num,end_num+1):
            url = self.url.format(str(i))
            all_url.append(url)
import threading



all_img_urls = []
g_lock = threading.Lock()
#todo:分析每页网站中的url地址
class HtmlUrl(threading.Thread):
    def run(self):
        headers = {
            'User-Agent':UserAgent().random
        }
        while len(all_url) > 0:
            g_lock.acquire()
            page_url = all_url.pop()
            g_lock.release()
            try:
                print('提取每章图片',page_url)
                response = requests.get(page_url,headers = headers)
                all_pic_link = re.findall('<a target=\'_blank\' href="(.*?)">',response.text,re.S)
                g_lock.acquire()
                global all_img_urls
                all_img_urls += all_pic_link
                print(all_img_urls)
                g_lock.release()
                time.sleep(0.5)
            except:
                pass
#todo 分析每个图片网站的各个图片的url地址
pic_links = []
class DownImage(threading.Thread):
    def run(self):
        global headers
        headers = headers
        global all_img_urls
        print('%s is runing'%threading.current_thread().name)
        while len(all_img_urls) > 0:
            g_lock.acquire()
            img_url = all_img_urls.pop()
            g_lock.release()
            try:
                response = requests.get(img_url,headers=headers)
                response.encoding='gb2312'   #由于我们调用的页面编码是GB2312，所以需要设置一下编码
                title = re.search('<title>(.*?) | 妹子图</title>',response.text).group(1)
                all_pic_src = re.findall('<img alt=.*?src="(.*?)" /><br />',response.text,re.S)
                pic_dict = {title:all_pic_src}   #python字典
                global pic_links
                g_lock.acquire()
                pic_links.append(pic_dict)    #字典数组
                print(title+" 获取成功")
                g_lock.release()
            except:
                pass
            time.sleep(0.5)
#todo:下载图片
class DownPic(threading.Thread):
    def run(self):
        global headers
        headers = headers
        while True:
            global  pic_links
            g_lock.acquire()
            if len(pic_links) == 0:
                g_lock.release()
                continue
            else:
                pic = pic_links.pop()
                g_lock.release()
                for key,values in  pic.items():
                    path=key.rstrip("\\")
                    is_exists=os.path.exists(path)
                    # 判断结果
                    if not is_exists:
                        # 如果不存在则创建目录
                        # 创建目录操作函数
                        os.makedirs(path)

                        print (path+'目录创建成功')

                    else:
                        # 如果目录存在则不创建，并提示目录已存在
                        print(path+' 目录已存在')
                    for pic in values :
                        filename = path+"/"+pic.split('/')[-1]
                        if os.path.exists(filename):
                            continue
                        else:
                            response = requests.get(pic,headers=headers)
                            with open(filename,'wb') as f :
                                f.write(response.content)
#todo 项目跑去主函数
if __name__ == '__main__':
    user = MeiZhi()
    user.html_url(5,7)
    threads = []
    for x in range(2):
        t = HtmlUrl()
        t.start()
        threads.append(t)
    for tt in threads:
        tt.join()
    for x in range(10):
        ta = DownImage()
        ta.start()
    for x in range(10):
        down = DownPic()
        down.start()







