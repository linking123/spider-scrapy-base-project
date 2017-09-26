# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# 注：存储结构化数据

import scrapy


class GanjizufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    money = scrapy.Field()
    roomsnum = scrapy.Field()
    square = scrapy.Field()
    direct = scrapy.Field()
    floor = scrapy.Field()
    decoration = scrapy.Field()
    community = scrapy.Field()
    address = scrapy.Field()
    pass


class Person(scrapy.Item):
    name = scrapy.Field()
    job = scrapy.Field()
    email = scrapy.Field()