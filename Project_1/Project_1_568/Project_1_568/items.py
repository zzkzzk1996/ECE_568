# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Project1568Item(scrapy.Item):
    # define the fields for your item here like:
    open = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    close = scrapy.Field()
    volume = scrapy.Field()
    stockname = scrapy.Field()
    _id = scrapy.Field()
    pass

