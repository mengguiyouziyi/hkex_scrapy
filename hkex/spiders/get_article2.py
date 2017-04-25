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
    name = 'get_article2'
    def start_requests(self):
        with codecs.open('hkex_cn.txt', 'r', 'utf-8') as file:
            hkex_cns = file.readlines()
        for index, hkex_cn in enumerate(hkex_cns):
            count = index + 1
            if count < 35583 or count > 65583: # 到8852
                continue
            request = scrapy.Request('http://www.hkexnews.hk'+hkex_cn.strip(), callback=self.parse_item)
            request.meta['count'] = count
            yield request

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
        if url.lower().endswith('_c.pdf'):
            base_url = '/'.join(url.split('/')[:-1]) + '/' # http://www.hkexnews.hk/listedco/listconews/SEHK/2016/1027/
            pdf_folder = base_folders[0] + name + '/'
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)

            article_name = name + '.pdf'
            article_path = os.path.join(pdf_folder, article_name)
            urlretrieve(url, article_path)
            # print('cn_pdf')

            url_test1 = url[:-6] + url[-4:]
            num_en = url.split('/')[-1][11:-6]  # LTN20161027393_C中的393,或064
            url_test2 = base_url + url.split('/')[-1][:11] + str(int(num_en) - 1).zfill(len(num_en)) + '.pdf'
            # 如果直接去_C可以返回（再次提交request），就取
            if self.test_url(url_test1) == 200:
                url_en = url_test1
                name_en = url_en.split('/')[-1].split('.')[-2]
                article_name_en = name_en + '.pdf'
                article_path_en = os.path.join(pdf_folder, article_name_en)
                # print('qian' + url_en)
                urlretrieve(url_en, article_path_en)
                # print('hou' + url_en)
                # print('en_pdf')
            elif self.test_url(url_test2) == 200:
                url_en = url_test2
                name_en = url_en.split('/')[-1].split('.')[-2]
                article_name_en = name_en + '.pdf'
                article_path_en = os.path.join(pdf_folder, article_name_en)
                # print('qian' + url_en)
                urlretrieve(url_en, article_path_en)
                # print('hou' + url_en)
                # print('en_pdf')

        elif url.lower().endswith('_c.xls'):
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
                # print('en_xls')
        elif url.lower().endswith('_c.doc'):
            base_url = '/'.join(url.split('/')[:-1]) + '/'
            doc_folder = base_folders[1] + name + '/'
            if not os.path.exists(doc_folder):
                os.makedirs(doc_folder)

            article_name = name + '.doc'
            article_path = os.path.join(doc_folder, article_name)
            urlretrieve(url, article_path)
            # print('cn_xls')

            url_test1 = url[:-6] + url[-4:]
            # print('1111111111111'+url_test1)
            num_en = url.split('/')[-1][11:-6]
            url_test2 = base_url + url.split('/')[-1][:11] + str(int(num_en) - 1) + '.doc'
            # print('2222222222222222'+url_test2)
            if self.test_url(url_test1) == 200:
                url_en = url_test1
                # print('========================' + url_en)
                name_en = url_en.split('/')[-1].split('.')[-2]
                article_name_en = name_en + '.doc'
                article_path_en = os.path.join(doc_folder, article_name_en)
                urlretrieve(url_en, article_path_en)
                # print('en_xls')
            elif self.test_url(url_test2) == 200:
                url_en = url_test2
                # print('========================' + url_en)
                name_en = url_en.split('/')[-1].split('.')[-2]
                article_name_en = name_en + '.doc'
                article_path_en = os.path.join(doc_folder, article_name_en)
                urlretrieve(url_en, article_path_en)
                # print('en_xls')



            # # 不用-1，去掉_C就是英文url。其他无区别
            # # 构造单个文件目录
            # doc_folder = base_folders[2] + name + '/'
            # if not os.path.exists(doc_folder):
            #     os.makedirs(doc_folder)
            # # 下载中文doc
            # article_name = name + '.doc'
            # article_path = os.path.join(doc_folder, article_name)
            # urlretrieve(url, article_path)
            # # print('cn_doc')
            #
            # # 下载英文doc
            # url_test1 = url[:-6] + url[-4:]
            # # 如果能返回，就构造英文链接
            # if self.test_url(url_test1) != 200:
            #     pass
            # url_en = url_test1
            # name_en = name[:-2]
            # article_name_en = name_en + '.doc'
            # article_path_en = os.path.join(doc_folder, article_name_en)
            # urlretrieve(url_en, article_path_en)
            # # print('en_doc')

        elif url.endswith('_C.HTM'):
            HTM_folder = base_folders[3] + name + '/'
            if not os.path.exists(HTM_folder):
                os.makedirs(HTM_folder)
            article_name = name + '.txt'
            article_path = os.path.join(HTM_folder, article_name)

            # 下载中文doc
            text = response.xpath('//pre/text()').extract()
            # print(type(text))
            # print(text)
            with codecs.open(article_path, 'a', 'utf-8') as file:
                file.writelines(text)
            # print('cn_HTM')

            # 下载英文doc
            url_test1 = url[:-6] + url[-4:]
            # print('HTM_url_en111' + url_test1)
            # 如果能返回，就构造英文链接
            # print('status' + str(self.test_url(url_test1)))
            if self.test_url(url_test1) != 200:
                pass
            url_en = url_test1
            # print('HTM_url_en222' + url_en)
            request = scrapy.Request(url_en, callback=self.parse_HTM_en)
            request.meta['name'] = name
            request.meta['HTM_folder'] = HTM_folder
            yield request
        else:
            pass

    def test_url(self, url):
        return requests.get(url).status_code

    def parse_HTM_en(self, response):
        name = response.meta['name']
        HTM_folder = response.meta['HTM_folder']
        text_en = response.xpath('//pre/text()').extract()
        # print(type(text_en))
        # print(text_en)

        name_en = name[:-2]
        article_name_en = name_en + '.txt'
        article_path_en = os.path.join(HTM_folder, article_name_en)
        with codecs.open(article_path_en, 'a', 'utf-8') as file:
            file.writelines(text_en)
        # print('en_HTM')









