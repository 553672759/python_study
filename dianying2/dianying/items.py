# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DianyingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    VideoTitle = scrapy.Field()
    VideoLink = scrapy.Field()
    VideoND = scrapy.Field()
    VideoContent = scrapy.Field()
    VideoPF = scrapy.Field()
    VideoImgName = scrapy.Field()
    VideoTag = scrapy.Field()
    VideoImg = scrapy.Field()
    #images = scrapy.Field()

