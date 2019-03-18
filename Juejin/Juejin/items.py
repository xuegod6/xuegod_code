# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JuejinItem(scrapy.Item):
    _id = scrapy.Field()
    username = scrapy.Field()
    job = scrapy.Field()
    company =scrapy.Field()
    intro = scrapy.Field()
    # 专栏
    columns = scrapy.Field()
    # 沸点
    boiling = scrapy.Field()
    # 分享
    shares = scrapy.Field()
    # 赞
    praises = scrapy.Field()
    books = scrapy.Field()
    # 关注了
    follow = scrapy.Field()
    # 关注者
    followers = scrapy.Field()
    goods = scrapy.Field()
    editer = scrapy.Field()
    reads = scrapy.Field()
    collections = scrapy.Field()
    tags = scrapy.Field()

