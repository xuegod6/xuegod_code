# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 15:38
# @Author  : for 
# @File    : 05_知乎_spider_test.py
# @Software: PyCharm
import time
import pymongo
from fake_useragent import UserAgent

import time
import requests
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
                if self._offset <= self._totle:
                    self._offset  = self._offset + 5 # 每次+5
                    print("防止被办，休息3s")
                    time.sleep(3)
                    self.run()
                else:
                    print("所有数据获取完毕")

if __name__ == '__main__':
    zhi = ZhiHuOne(1084)
    zhi.run()




