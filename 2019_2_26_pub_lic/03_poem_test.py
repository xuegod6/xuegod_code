# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 10:43
# @Author  : for 
# @File    : 03_poem_test.py
# @Software: PyCharm
import re
import requests
from bs4 import BeautifulSoup

from fake_useragent import UserAgent

from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED

urls = ['https://so.gushiwen.org/gushi/tangshi.aspx',
        'https://so.gushiwen.org/gushi/sanbai.aspx',
        'https://so.gushiwen.org/gushi/songsan.aspx',
        'https://so.gushiwen.org/gushi/songci.aspx'
        ]
poem_links = []

for url in urls:
    ua = UserAgent()
    headers = {'User-Agent':ua.random}
    req = requests.get(url,headers = headers)

    soup = BeautifulSoup(req.text,'lxml')
    content = soup.find_all('div',class_='sons')[0]

    links = content.find_all('a')
    for link in links:
        poem_links.append('https://so.gushiwen.org'+link['href'])

poem_list = []
def get_poem(url):
    ua = UserAgent()
    headers = {'User-Agent':ua.random}
    req = requests.get(url,headers = headers)
    soup = BeautifulSoup(req.text,'lxml')
    poem = soup.find('div',class_='contson').text.strip()
    poem = poem.replace(' ', '')
    poem = re.sub(re.compile(r"\([\s\S]*?\)"), '', poem)
    poem = re.sub(re.compile(r"（[\s\S]*?）"), '', poem)
    poem = re.sub(re.compile(r"。\([\s\S]*?）"), '', poem)
    poem = poem.replace('!', '!').replace('?', '？')
    poem_list.append(poem)

executor = ThreadPoolExecutor(max_workers=10)
future_tasks = [executor.submit(get_poem,url)for url in poem_links]

wait(future_tasks,return_when=ALL_COMPLETED)

# 将爬取的诗句写入txt文件
poems = list(set(poem_list))
poems = sorted(poems, key=lambda x:len(x))
print(poems)
for poem in poems:
    poem = poem.replace('《','').replace('》','').replace('：', '').replace('“', '')
    print(poem)
    with open('poem.txt', 'a',encoding='utf-8') as f:
        f.write(poem)
        f.write('\n')


