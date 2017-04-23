# -*- coding: utf-8 -*-
import scrapy
import codecs

class NormalSpider(scrapy.Spider):
    name = "normal"
    allowed_domains = ["hkexnews.hk"]
    def __init__(self):
        self.base_url = 'http://www.hkexnews.hk'

    def start_requests(self):
        with codecs.open('111pdf_doc_url.txt', 'r', 'utf-8') as file:
            viewstates = file.readlines()
        for viewstate in viewstates:
            yield scrapy.FormRequest(url='http://www.hkexnews.hk/listedco/listconews/advancedsearch/search_active_main_c.aspx',
                                     formdata={'__VIEWSTATE':viewstate.strip(), '__VIEWSTATEENCRYPTED': '' ,'__VIEWSTATEGENERATOR': 'C344FAEC',},
                                     callback=self.parse)

    def parse(self, response):
        news = response.xpath('//a[@class="news"]/@href').extract()
        for new in news:
            print(self.base_url + new)
        ass = response.xpath('//input[@id="__VIEWSTATE"]/@value').extract()[0]
        next_page = response.xpath('//input[@id="ctl00_btnNext"]/@src').extract()
        if len(next_page) != 0:
            yield scrapy.FormRequest(
                url='http://www.hkexnews.hk/listedco/listconews/advancedsearch/search_active_main_c.aspx',
                formdata={'__VIEWSTATE': ass, '__VIEWSTATEENCRYPTED': '', '__VIEWSTATEGENERATOR': 'C344FAEC', "ctl00$btnNext.x": "25", "ctl00$btnNext.y": "9",},
                callback=self.parse,)










