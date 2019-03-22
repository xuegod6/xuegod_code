# -*- coding: utf-8 -*-
import scrapy

from tencent1.items import Tencent1Item

# positionname = scrapy.Field()
# positionline = scrapy.Field()
# positionType = scrapy.Field()
# positionNum = scrapy.Field()
# workLocation = scrapy.Field()
# publishTime = scrapy.Field()
class TencentSpider(scrapy.Spider):
    url='https://hr.tencent.com/position.php?&start='
    offset = 0
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = [url + str(offset)]
    def parse(self, response):
        for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            item = Tencent1Item()
            item['positionname'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['positionline'] = each.xpath('./td[1]/a/@href').extract()[0]
            try:
                item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            except Exception as e:
                pass
            item['positionNum'] = each.xpath('./td[3]/text()').extract()[0]
            item['workLocation'] = each.xpath('./td[4]/text()').extract()[0]
            item['publishTime'] = each.xpath('./td[5]/text()').extract()[0]
            yield item
        # pass
        if self.offset < 1000:
            self.offset += 10
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)
