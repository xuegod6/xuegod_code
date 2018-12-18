# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentTestItem(scrapy.Item):
    positionname = scrapy.Field()
    positionlink = scrapy.Field()
    positionType = scrapy.Field()
    peopleNum = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime = scrapy.Field()

