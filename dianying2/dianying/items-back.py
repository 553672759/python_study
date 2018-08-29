# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DianyingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    video_name = scrapy.Field()
    video_link = scrapy.Field()
    video_nd = scrapy.Field()
    video_cd = scrapy.Field()
    video_pf = scrapy.Field()
    vidoe_dy = scrapy.Field()
    video_img = scrapy.Field()
    vidoe_jj = scrapy.Field()
    video_type = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()

