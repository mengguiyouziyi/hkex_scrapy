# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider

class HkexSpider(CrawlSpider):
    name = 'redirect'
    start_urls = ['http://www.hkexnews.hk/listedco/listconews/mainindex/SEHK_LISTEDCO_DATETIME_TODAY.HTM']

    def parse_item(self, response):
        print(response.url)
        print(response.body_as_unicode())









