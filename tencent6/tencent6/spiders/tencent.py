# -*- coding: utf-8 -*-
import scrapy

from tencent6.items import Tencent6Item
# positionname = scrapy.Field()
# positionlink = scrapy.Field()
# positionType = scrapy.Field()
# peopleNum = scrapy.Field()
# workLocation = scrapy.Field()
# publishTime = scrapy.Field()

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    offset = 0
    url = 'https://hr.tencent.com/position.php?&start='
    start_urls = [url + str(offset)]
    def parse(self, response):
        for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            item = Tencent6Item()
            item['positionname'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['positionlink'] = each.xpath('./td[1]/a/@href').extract()[0]
            try:

                item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            except IndexError:
                pass
            item['peopleNum'] = each.xpath('./td[3]/text()').extract()[0]
            item['workLocation'] = each.xpath('./td[4]/text()').extract()[0]
            item['publishTime'] = each.xpath('./td[5]/text()').extract()[0]
            yield item

        if self.offset < 1000:
            self.offset += 10
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)



