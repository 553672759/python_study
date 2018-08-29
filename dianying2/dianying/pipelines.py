# -*- coding: utf-8 -*-

from pymongo import MongoClient
import scrapy
import MySQLdb
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DianyingPipeline(object):
    def __init__(self):

        dbargs = dict(
        host = '127.0.0.1:3306',
        db = 'myweb',
        user = 'root',  # replace with you user name
        passwd = '123456',  # replace with you password
        charset = 'utf8',
        cursorclass = MySQLdb.cursors.DictCursor,
        use_unicode = True,
        )

        def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item


#
# class MzituScrapyPipeline(ImagesPipeline):
#
#     def get_media_requests(self, item, info):
#         for image_url in item['image_urls']:
#             yield scrapy.Request(image_url)
#
#     def item_completed(self, results, item, info):
#         image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem("Item contains no images")
#         item['image_paths'] = image_paths
#         return item


