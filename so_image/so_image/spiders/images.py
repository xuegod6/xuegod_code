# -*- coding: utf-8 -*-
import scrapy
import json

class ImagesSpider(scrapy.Spider):
    BASE_URL = 'http://image.so.com/zj?ch=beauty&sn=%s&listtype=new&temp=1'
    name = 'images'
    start_index = 0
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/zj?ch=beauty&sn=0&listtype=new&temp=1']
    MAX_DOWNLOAD_NUM = 1000
    def parse(self, response):

        infos = json.loads(response.body.decode('utf-8'))

        yield {'image_urls':[info['qhimg_url']for info in infos['list']]}
    #count = 30
        self.start_index += infos['count']
        # 30 - 60 -90
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
#BASE_URL = 'http://image.so.com/zj?ch=beauty&sn=%s&listtype=new&temp=1'%60
            yield  scrapy.Request(self.BASE_URL%self.start_index)

