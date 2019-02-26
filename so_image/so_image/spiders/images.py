# -*- coding: utf-8 -*-
import scrapy,json
from so_image.items import SoImageItem

class ImagesSpider(scrapy.Spider):
    #这是基础的请求地址
    BASE_URL = 'http://image.so.com/zj?ch=art&sn=%s&listtype=new&temp=1'
    name = 'images'#项目名称
    start_index = 0#给个数字 方便后期拼接
    allowed_domains = ['image.so.com']#域名允许爬取的域名
    #开爬取时候的地址
    start_urls = ['http://image.so.com/zj?ch=art&sn=0&listtype=new&temp=1']
    MAX_DOWNLOAD_NUM = 1000#最大的数据量图片量
#http://image.so.com/zj?ch=art&sn=30&listtype=new&temp=1
# http://image.so.com/zj?ch=art&sn=60&listtype=new&temp=1
# http://image.so.com/zj?ch=art&sn=90&listtype=new&temp=1
    def parse(self, response):
        #response 是响应的数据，他是一个json
        #json方法 吧数据编程python可操作性对象
        infos = json.loads(response.body.decode('utf-8'))
        #生成器，把数据交给items，注意键名一定对应items中的字段
        yield {'image_urls':[info["qhimg_url"]for info in infos['list']]}
        self.start_index += infos['count']#自增，为了 拼接url地址
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            #重新进行请求
            yield scrapy.Request(self.BASE_URL%self.start_index)

