# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

from Juejin.items import JuejinItem
class JuejinSpider(scrapy.Spider):
    name = 'juejin'
    allowed_domains = ['juejin.im']
    start_urls = ['https://juejin.im/user/55fa7cd460b2e36621f07dde/following']
    def get_default(self,exts):
        if len(exts)>0:
            ret = exts[0]
        else:
            ret = 0
        return ret

    def parse(self, response):
        #base_data = response.body_as_unicode()
        select = Selector(response)
        item = JuejinItem()
        # 这个地方获取一下数据
        item["username"] = select.xpath("//h1[@class='username']/text()").extract()[0]
        position = select.xpath("//div[@class='position']/span/span/text()").extract()
        if position:
            job = position[0]
            if len(position)>1:
                company = position[1]
            else:
                company = ""
        else:
            job = company = ""
        item["job"] = job
        item["company"] = company
        item["intro"] = self.get_default(select.xpath("//div[@class='intro']/span/text()").extract())
        # 专栏
        item["columns"] = self.get_default(select.xpath("//div[@class='header-content']/a[2]/div[2]/text()").extract())
        # 沸点
        item["boiling"] = self.get_default(select.xpath("//div[@class='header-content']/a[3]/div[2]/text()").extract())
        # 分享
        item["shares"] = self.get_default(select.xpath("//div[@class='header-content']/a[4]/div[2]/text()").extract())
        # 赞
        item["praises"] = self.get_default(select.xpath("//div[@class='header-content']/a[5]/div[2]/text()").extract())
        #
        item["books"] = self.get_default(select.xpath("//div[@class='header-content']/a[6]/div[2]/text()").extract())

        # 关注了
        item["follow"] = self.get_default(select.xpath("//div[@class='follow-block block shadow']/a[1]/div[2]/text()").extract())
        # 关注者
        item["followers"] = self.get_default(select.xpath("//div[@class='follow-block block shadow']/a[2]/div[2]/text()").extract())


        right = select.xpath("//div[@class='stat-block block shadow']/div[2]/div").extract()
        if len(right) == 3:
            item["editer"] = self.get_default(select.xpath("//div[@class='stat-block block shadow']/div[2]/div[1]/span/text()").extract())
            item["goods"] = self.get_default(select.xpath("//div[@class='stat-block block shadow']/div[2]/div[2]/span/span/text()").extract())
            item["reads"] = self.get_default(select.xpath("//div[@class='stat-block block shadow']/div[2]/div[3]/span/span/text()").extract())

        else:
            item["editer"] = ""
            item["goods"] = self.get_default(select.xpath("//div[@class='stat-block block shadow']/div[2]/div[1]/span/span/text()").extract())
            item["reads"] = self.get_default(select.xpath("//div[@class='stat-block block shadow']/div[2]/div[2]/span/span/text()").extract())

        item["collections"] = self.get_default(select.xpath("//div[@class='more-block block']/a[1]/div[2]/text()").extract())
        item["tags"] = self.get_default(select.xpath("//div[@class='more-block block']/a[2]/div[2]/text()").extract())
        yield item  # 返回item

        list_li = select.xpath("//ul[@class='tag-list']/li")  # 获取所有的关注
        for li in list_li:
            a_link = li.xpath(".//meta[@itemprop='url']/@content").extract()[0] # 获取URL
            # 返回拼接好的数据请求
            yield scrapy.Request(a_link+"/following",callback=self.parse)
