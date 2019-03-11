# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:46
# @Author  : for 
# @File    : 03_baisi_test.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import requests
import re,time
url = 'http://www.budejie.com/video/'
def get_page_url(url,data=None):
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
    }
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,'html.parser')
    lists = soup.find_all('a',href = re.compile('http://svideo.spriteapp.com/video/2019/(.*?).mp4'))
    print(lists)
    a = 0
    for i in lists:
        a += 1
        url_href = i.get('href')
        print(url_href)
        req = requests.get(url_href)
        print('num'+str(a)+'video')
        with open(str(time.time())+'.mp4','wb')as file:
            file.write(req.content)
def get_more_pages(start,end):
    for one in range(start,end):
        get_page_url(url+str(one))
        time.sleep(0.2)
if __name__ == '__main__':
    get_more_pages(1,3)