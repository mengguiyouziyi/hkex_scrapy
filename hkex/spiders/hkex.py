# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import codecs
from urllib.request import urlretrieve
import os.path
# from scrapy import selector
# from django.utils.html import strip_tags
# import re

class HkexSpider(CrawlSpider):
    name = 'hkex'
    # allowed_domains = ['hkex.com.hk', 'hkex.hk']
    start_urls = ['http://www.hkexnews.hk/listedco/listconews/mainindex/SEHK_LISTEDCO_DATETIME_TODAY.HTM']

    rules = (
        # Rule(LinkExtractor(allow=''), follow=True),
        Rule(LinkExtractor(allow='pdf'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.status)
        print(response.url)
        # print(response.body_as_unicode())
        # with codecs.open('aa.html', 'a', 'utf-8') as f:
        #     f.writelines(response.body_as_unicode())

        # 记录pdf url
        # with codecs.open('pdf_url.txt', 'a', 'utf-8') as f:
        #     f.writelines(response.url)
        # # 下载pdf文件
        # article_name = response.url.split('/')[-1]
        # save_folder = "./download/"
        # if not os.path.exists(save_folder):
        #     os.makedirs(save_folder)
        # article_path = os.path.join(save_folder, article_name)
        # urlretrieve(response.url, article_path)
















        # 先选择body中的内容
        # 再去掉<script>中的内容


        # html = response.body_as_unicode()
        # print(type(html))
        # print(text)

        # aa = response.xpath('//body').extract()[0]
        # print(aa)
        # text, number = re.subn(r'<script>.*</script>', '', aa)
        # print(text)
        # print(number)
        # with codecs.open('y.txt', 'w', 'utf-8') as file:
        #     for a in aa:
        #         file.writelines(a)
        # text = strip_tags(aa)
