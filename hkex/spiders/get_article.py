# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
import codecs
import scrapy
import os
import os.path

class HkexSpider(CrawlSpider):
    name = 'get_article'
    def start_requests(self):
        with codecs.open('hkex_cn_test.txt', 'r', 'utf-8') as file:
            hkex_cns = file.readlines()
        for hkex_cn in hkex_cns:
            yield scrapy.Request(hkex_cn.strip(), callback=self.parse_item)

    def parse_item(self, response):
        # http://www.hkexnews.hk/listedco/listconews/SEHK/2016/1027/LTN20161027393_C.pdf
        base_folders = ['./download/pdf/', './download/xls/', './download/doc/', './download/htm/', './download/other/',]
        for base_folder in base_folders:
            if os.path.exists(base_folder):
                os.makedirs(base_folder)
        url = response.url

        if url.lower().endswith('_c.pdf') or url.lower().endswith('_c.xls'):
            folder = url.split('/')[-1].split('.')[-2]


            base_url = '/'.join(url.split('/')[:-1]) + '/'
            num = int(url.split('/')[-1][11:-6])
            url_en = base_url + url.split('/')[-1][:12] + str(num - 1) + '.pdf'

        elif url.lower().endswith('_c.doc') or url.lower().endswith('_c.htm'):
            folder = url.split('/')[-1].split('.')[-2]
            url_en = url[:-6] + url[-4:]
            if url.lower().endswith('_c.doc'):
                pass
            else:
                pass
        else:
            pass











