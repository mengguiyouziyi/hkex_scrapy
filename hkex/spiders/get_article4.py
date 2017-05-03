# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
import codecs
import scrapy
import os
import os.path
from urllib.request import urlretrieve
import requests
import re

# http://101.96.10.26/www.hkexnews.hk/listedco/listconews/GEM/2016/1027/GLN2016102763.pdf
class HkexSpider(CrawlSpider):
    name = 'get_article5'
    def start_requests(self):
        with codecs.open('hkex_cn.txt', 'r', 'utf-8') as file:
            hkex_cns = file.readlines()
        for index, hkex_cn in enumerate(hkex_cns):
            count = index + 1
            # if count < 125583:
            #     continue
            if hkex_cn.strip().lower().endswith('_c.xls'):
                yield scrapy.Request(url='http://www.hkexnews.hk'+hkex_cn.strip(), meta={'count':count}, callback=self.parse_item)

    def parse_item(self, response):
        count = response.meta['count']
        # http://www.hkexnews.hk/listedco/listconews/SEHK/2016/1027/LTN20161027393_C.pdf
        base_folders = ['./download/pdf/', './download/xls/', './download/doc/', './download/HTM/', './download/other/',]
        for base_folder in base_folders:
            if not os.path.exists(base_folder):
                os.makedirs(base_folder)
        url = response.url
        # print('##################################'+url)
        url, number = re.subn(r'\d+\.\d+\.\d+\.\d+\/', '', url)
        print(('%s@' % str(count)) + url)
        if '.' not in url.split('/')[-1]:
            pass
        name = url.split('/')[-1].split('.')[-2] # 纯文件名，如LTN20161027393_C
        base_url = '/'.join(url.split('/')[:-1]) + '/'
        xls_folder = base_folders[1] + name + '/'
        if not os.path.exists(xls_folder):
            os.makedirs(xls_folder)

        article_name = name + '.xls'
        article_path = os.path.join(xls_folder, article_name)
        urlretrieve(url, article_path)
        # print('cn_xls')

        url_test1 = url[:-6] + url[-4:]
        # print('1111111111111'+url_test1)
        num_en = url.split('/')[-1][11:-6]
        url_test2 = base_url + url.split('/')[-1][:11] + str(int(num_en) - 1) + '.xls'
        url_test3 = base_url + url.split('/')[-1][:11] + str(int(num_en) + 1) + '.xls'
        # print('2222222222222222'+url_test2)
        if self.test_url(url_test1) == 200:
            url_en = url_test1
            # print('========================' + url_en)
            name_en = url_en.split('/')[-1].split('.')[-2]
            article_name_en = name_en + '.xls'
            article_path_en = os.path.join(xls_folder, article_name_en)
            urlretrieve(url_en, article_path_en)
            # print('en_xls')
        elif self.test_url(url_test2) == 200:
            url_en = url_test2
            # print('========================' + url_en)
            name_en = url_en.split('/')[-1].split('.')[-2]
            article_name_en = name_en + '.xls'
            article_path_en = os.path.join(xls_folder, article_name_en)
            urlretrieve(url_en, article_path_en)
        elif self.test_url(url_test3) == 200:
            url_en = url_test3
            # print('========================' + url_en)
            name_en = url_en.split('/')[-1].split('.')[-2]
            article_name_en = name_en + '.xls'
            article_path_en = os.path.join(xls_folder, article_name_en)
            urlretrieve(url_en, article_path_en)

    def test_url(self, url):
        try:
            status_code = requests.get(url).status_code
            return status_code
        except Exception as e:
            print(e)
            return 0









