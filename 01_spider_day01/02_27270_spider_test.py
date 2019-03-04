# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 11:11
# @Author  : for 
# @File    : 02_27270_spider_test.py
# @Software: PyCharm
import os
import re
import threading
import time

import requests,random,datetime
from retrying import retry
from fake_useragent import UserAgent
headers = {
    'User-Agent':UserAgent().random
}
class R:
    def __init__(self,method="get",params=None,headers=None,cookies=None):
        self.__method = method
        myheaders = self.get_headers()
        if headers is not None:
            myheaders.update(headers)
        self.__headers = myheaders
        self.__cookies = cookies
        self.__params = params

        pass
    def get_headers(self):
        return headers
    @retry(stop_max_attempt_number = 3)
    def __retrying_requests(self,url):
        pass
    def get_content(self,url,charset = 'utf-8'):
        try:
            html_str = self.__retrying_requests(url).decode(charset)
        except:
            html_str =  None
        return html_str
    def get_file(self,file_url):
        try:
            file= self.__retrying_requests(file_url)
        except:
            file = None
        return file
class ImageList():
    def __init__(self):
        self.__start = "http://www.27270.com/ent/meinvtupian/list_11_{}.html"
        self.__headers = headers
        self.__res = R(headers = self.__headers)
    def run(self):
        page_count =  int(self.get_page_count())
        if page_count==0:
            return
        urls = [self.__start.format(i) for i in range(1,page_count)]
        return urls

    def get_page_count(self):
        content = self.__res.get_content(self.__start.format("1"),"gb2312")
        pattern = re.compile("<li><a href='list_11_(\d+?).html' target='_self'>末页</a></li>")
        search_text = pattern.search(content)
        if search_text is not None:
            count = search_text.group(1)
            return count
        else:
            return 0
urls_lock = threading.Lock()  #url操作锁
imgs_lock = threading.Lock()  #图片操作锁

imgs_start_urls = []


class Product(threading.Thread):
    # 类的初始化方法
    def __init__(self,urls):
        threading.Thread.__init__(self)
        self.__urls = urls
        self.__headers = {"Referer":"http://www.27270.com/ent/meinvtupian/",
                          "Host":"www.27270.com"
                          }

        self.__res = hh.R(headers=self.__headers)

    # 链接抓取失败之后重新加入urls列表中
    def add_fail_url(self,url):
        print("{}该URL抓取失败".format(url))
        global urls_lock
        if urls_lock.acquire():
            self.__urls.insert(0, url)
            urls_lock.release()  # 解锁

    # 线程主要方法
    def run(self):
        print("*"*100)
        while True:
            global urls_lock,imgs_start_urls
            if len(self.__urls)>0:
                if urls_lock.acquire():   # 锁定
                    last_url = self.__urls.pop()   # 获取urls里面最后一个url，并且删除
                    urls_lock.release()  # 解锁

                print("正在操作{}".format(last_url))

                content = self.__res.get_content(last_url,"gb2312")   # 页面注意编码是gb2312其他格式报错
                if content is not  None:
                    html = self.get_page_list(content)

                    if len(html) == 0:
                        self.add_fail_url(last_url)
                    else:
                        if imgs_lock.acquire():
                            imgs_start_urls.extend(html)    # 爬取到图片之后，把他放在待下载的图片列表里面
                            imgs_lock.release()

                    time.sleep(5)
                else:
                    self.add_fail_url(last_url)

            else:
                print("所有链接已经运行完毕")
                break





    def get_page_list(self,content):
        # 正则表达式
        pattern = re.compile('<li> <a href="(.*?)" title="(.*?)" class="MMPic" target="_blank">.*?</li>')
        list_page = re.findall(pattern, content)

        return list_page
class Consumer(threading.Thread):
    # 初始化
    def __init__(self):
        threading.Thread.__init__(self)
        self.__headers = {"Referer": "http://www.27270.com/ent/meinvtupian/",
                          "Host": "www.27270.com"}
        self.__res = R(headers=self.__headers)

    # 图片下载方法
    def download_img(self,filder,img_down_url,filename):
        file_path = "./downs/{}".format(filder)

        # 判断目录是否存在，存在创建
        if not os.path.exists(file_path):
            os.mkdir(file_path)  # 创建目录

        if os.path.exists("./downs/{}/{}".format(filder,filename)):
            return
        else:
            try:
                # 这个地方host设置是个坑，因为图片为了防止盗链，存放在另一个服务器上面
                img = requests.get(img_down_url,headers={"Host":"t2.hddhhn.com"},timeout=3)
            except Exception as e:
                print(e)

            print("{}写入图片".format(img_down_url))
            try:
                # 图片写入不在赘述
                with open("./downs/{}/{}".format(filder,filename),"wb+") as f:
                    f.write(img.content)
            except Exception as e:
                print(e)
                return





    def run(self):

        while True:
            global imgs_start_urls,imgs_lock

            if len(imgs_start_urls)>0:
                if imgs_lock.acquire():  # 锁定
                    img_url = imgs_start_urls[0]   #获取到链接之后
                    del imgs_start_urls[0]  # 删掉第0项
                    imgs_lock.release()  # 解锁
            else:
                continue

            # http://www.27270.com/ent/meinvtupian/2018/295631_1.html

            #print("图片开始下载")
            img_url = img_url[0]
            start_index = 1
            base_url = img_url[0:img_url.rindex(".")]    # 字符串可以当成列表进行切片操作

            while True:

                img_url ="{}_{}.html".format(base_url,start_index)   # url拼接
                content = self.__res.get_content(img_url,charset="gbk")   # 这个地方获取内容，采用了gbk编码
                if content is not None:
                    pattern = re.compile('<div class="articleV4Body" id="picBody">[\s\S.]*?img alt="(.*?)".*? src="(.*?)" />')
                    # 匹配图片，匹配不到就代表本次操作已经完毕
                    img_down_url = pattern.search(content)  # 获取到了图片地址

                    if img_down_url is not None:
                        filder = img_down_url.group(1)
                        img_down_url = img_down_url.group(2)
                        filename = img_down_url[img_down_url.rindex("/")+1:]
                        self.download_img(filder,img_down_url,filename)  #下载图片

                    else:
                        print("-"*100)
                        print(content)
                        break # 终止循环体

                else:
                    print("{}链接加载失败".format(img_url))

                    if imgs_lock.acquire():  # 锁定
                        imgs_start_urls.append(img_url)
                        imgs_lock.release()  # 解锁

                start_index+=1   # 上文描述中，这个地方需要不断进行+1操作


if __name__ == '__main__':
    img = ImageList()
    urls = img.run()
    for i in range(1,2):
        p = Product(urls)
        p.start()
    for i in range(1,2):
        c = Consumer()
        c.start()