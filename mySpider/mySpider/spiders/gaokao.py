# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy import FormRequest
from fake_useragent import UserAgent
ua = UserAgent()
from mySpider.items import MyspiderItem
class GaokaoSpider(scrapy.Spider):
    #爬虫名字 必须唯一 不同爬虫需要定义不同的名字
    name = 'gaokao'
    #域名范围
    allowed_domains = ['www.gaokaopai.com']
    start_urls = 'http://www.gaokaopai.com/rank-index.html'
    def __init__(self):
        self.headers={
            'User-Agent':ua.random,
            "X-Requested-With":"XMLHttpRequest"
        }
    def start_requests(self):
        for page in range(0,7):
            form_data = {
                'otype': '4',
                'city':'',
                'start': str(25*page),
                'amount':'25',
            }
            request = FormRequest(self.start_urls,headers=self.headers,formdata=form_data,callback=self.parse)
            yield request
    def parse(self, response):
        #print(response.body)
        #print(response.url)
        #print(response.body)
        #获取到请求头
        content_type = response.headers['Content-Type']
        #进行判断
        if content_type.decode().find("text/html") > 0:
            trs = response.xpath("//table[@id='results']//tr")[1:]
            for item in trs:
                school = MyspiderItem()
                rank = item.xpath("td[1]/span/text()").extract()[0]
                uni_name = item.xpath("td[2]/a/text()").extract()[0]
                safehard  = item.xpath("td[3]/text()").extract()[0]
                city_code = item.xpath("td[4]/text()").extract()[0]
                uni_type = item.xpath("td[6]/text()").extract()[0]
                school["uni_name"] = uni_name
                school["uni_id"] = ""
                school["city_code"] = city_code
                school["uni_type"] = uni_type
                school["slogo"] = ""
                school["rank"] = rank
                school["safehard"] = safehard
                yield school
        else:
            #如果是json数据
            data = json.loads(response.body_as_unicode())
            data = data["data"]["ranks"] # 获取数据
            for item in data:
                school = MyspiderItem()
                school["uni_name"] = item["uni_name"]
                school["uni_id"] = item["uni_id"]
                school["city_code"] = item["city_code"]
                school["uni_type"] = item["uni_type"]
                school["slogo"] = item["slogo"]
                school["rank"] = item["rank"]
                school["safehard"] = item["safehard"]
                # 将获取的数据交给pipelines，pipelines在settings.py中定义
                yield school
        #
