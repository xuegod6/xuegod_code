# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 15:09
# @Author  : for 
# @File    : 01_csdn_spider_test.py
# @Software: PyCharm
import time

import requests
from fake_useragent import UserAgent
base_url = 'https://blog.csdn.net/api/articles?type=more&category=home&shown_offset={}'
start_url = 'https://blog.csdn.net/api/articles?type=more&category=home&shown_offset=1552547237739714'
ua = UserAgent()
headers = {
    'User-Agent':ua.random
}
import time


def get_url(url):
    try:
        response = requests.get(url=start_url,headers=headers)
    except:
        response = requests.get(url=start_url,headers=headers)
    else:
        json_data = response.json()
        if json_data['status']:
            with open('1.txt','a',encoding='utf-8') as f:
                art_datas = json_data['articles']
                for i in art_datas:
                    f.writelines(i['category_id']+'--'+i['nickname']+'--'+i['title']+'--'+i['url']+'\n')
        get_http(json_data['shown_offset'])
def get_http(offset):
    url = base_url.format(offset)
    print(url)
    get_url(url)
if __name__ == '__main__':
    get_url(start_url)

