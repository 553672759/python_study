# -*- coding: utf-8 -*-
import pymysql
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DianyingPipeline(object):

    def __init__(self):

        #连接数据库
        self.con=pymysql.connect(
            host="127.0.0.1",
            db="myweb",
            user="root",
            passwd="123456",
            charset='utf8',
            use_unicode=True
        )

        # 通过cursor执行增删查改
        self.cue = self.con.cursor();

    def process_item(self,item,spider):

        print("mysql connect succes")
        self.cue.execute("""insert into Videos(VideoId, VideoTitle, VideoLink, VideoND ,VideoContent, VideoPF,VideoImgName,VideoTag,VideoImg)values (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                [item['VideoId'],
                 item['VideoTitle'],
                 item['VideoLink'],
                 item['VideoND'],
                 item['VideoContent'],
                 item['VideoPF'],
                 item['VideoImgName'],
                 item['VideoTag'],
                 item['VideoImg']
                 ])
        print("insert success")
        #提交sql语句
        self.con.commit()
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


