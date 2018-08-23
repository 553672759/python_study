# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Request, Rule
from dianying.items import DianyingItem
# scrapy crawl spidertieba -o items.json



class dianying(scrapy.Spider):
    name = "dianying"
    allowed_domains = ["www.dy2018.com"]
    i=98000
    url = "https://www.dy2018.com/i/"
    start_urls = [url+str(i)+".html"]

    def parse(self, response):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        print self.start_urls[0]
        items = DianyingItem()
        #取得名字
        a = response.xpath('//*[@id="header"]/div/div[3]/div[2]/div[6]/div[1]/h1/text()').extract()[0]
        items['name'] = a
        #取得链接
        link=response.xpath('//*[@id="Zoom"]/table[2]/tbody/tr/td/a/@href').extract()
        if(not len(link) == 0):
            items['link'] =link
            yield items
        if self.i < 98050:
            self.i+=1
            yield scrapy.Request(self.url+str(self.i)+".html",callback=self.parse)



