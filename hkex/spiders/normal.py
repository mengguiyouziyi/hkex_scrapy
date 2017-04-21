# -*- coding: utf-8 -*-
import scrapy


class NormalSpider(scrapy.Spider):
    name = "normal"
    allowed_domains = ["www.hkexnews.hk"]
    start_urls = ['http://www.hkexnews.hk/listedco/listconews/mainindex/SEHK_LISTEDCO_DATETIME_TODAY.HTM/']

    def parse(self, response):
        print(response.body_as_unicode())