# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 15:38
# @Author  : for
# @File    : 05_知乎_spider_test.py
# @Software: PyCharm
import time
import pymongo
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as BS

import time
import requests
import re
#todo 给定mongodb一个ip 和端口
DATABASE_IP = '127.0.0.1'
DATABASE_PORT = 27017
#这个是给定数据库的名字
DATABASE_NAME = 'sun'
#接下来链接mangodb数据库
client = pymongo.MongoClient(DATABASE_IP,DATABASE_PORT)
#链接sun 数据库
db = client.sun
# db.authenticate("dba", "dba")
collection = db.zhihuone  # 准备插入数据
ua = UserAgent()
class ZhiHuOne():
    headers={
        "upgrade-insecure-requests":"1",
        'user-agent':ua.random,
    }
    def __init__(self,totle):
        self._offset = 0
        self._totle = totle
    def run(self):
        print('正在抓取{}的数据'.format(self._offset))
        with requests.session() as s:
            try:
                with s.get("https://www.zhihu.com/api/v4/questions/292393947/answers?include=comment_count,content,voteup_count,reshipment_settings,is_author,voting,is_thanked,is_nothelp;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=5&offset={}&sort_by=default".format(self._offset),headers=self.headers,timeout=3) as rep:
                    data =  rep.json()

                    if data:
                        collection.insert_many(data["data"])
            except Exception as e:
                print(e.args)
            finally:
                if self._offset != self._totle:
                    self._offset  = self._offset + 5 # 每次+5
                    print("防止被办，休息3s")
                    time.sleep(3)
                    self.download_img(data)#先下载图片
                    self.run()
                else:
                    print("所有数据获取完毕")
    def download_img(self,data):
        ## 下载图片
        for item in data["data"]:
            content = item["content"]
            pattern = re.compile('<noscript>(.*?)</noscript>')
            imgs = pattern.findall(content)
            if len(imgs) > 0:
                for img in imgs:
                    try:
                        match = re.search(r'<imgs src="(.*?)"', img)
                        download = match.groups()[0]
                    except:
                        match = re.search(r'<imgs src="(.*?)"', img)
                        download = match.groups()[0]
                    download = download.replace("pic3", "pic2")  # 小BUG,pic3的下载不到
                    print("正在下载{}".format(download), end="")
                    try:
                        with requests.Session() as s:
                            with s.get(download) as img_down:
                                # 获取文件名称
                                file = download[download.rindex("/") + 1:]
                                content = img_down.content
                                with open("imgs/{}".format(file), "wb+") as f:  # 这个地方进行了硬编码
                                    f.write(content)
                                print("图片下载完成", end="\n")
                    except Exception as e:
                        print(e.args)
            else:
                pass
BASE_URL = 'https://www.zhihu.com/question/{}'
def get_totle_answers(article_id):
    headers={
        'user-agent':ua.random,
    }
    with requests.Session() as s:
        with s.get(BASE_URL.format(article_id),headers=headers) as rep:
            html = rep.text
            bs_html = BS(html,'html.parser')
            # data = bs_html.find_all('meta',itemprop='answerCount')
            data = bs_html.find('meta',attrs={'itemprop':'answerCount'})
            result = data['content']
            return  result
if __name__ == '__main__':
    article_id = ''
    while not article_id.isdigit():
        article_id = input('请输入文章的ID:')
    totle = get_totle_answers(article_id)
    if int(totle) > 0:
        zhi = ZhiHuOne(int(totle))
        zhi.run()
    else:
        print('没有任何数据！')




