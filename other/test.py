#coding:utf-8
import requests
import codecs
import base64
import re

# url = 'http://www.hkexnews.hk/listedco/listconews/SEHK/2016/1027/LTN20161027393.pdf'
# res = requests.get(url)
# print(res.status_code)
url = 'http://101.96.10.26/www.hkexnews.hk/listedco/listconews/GEM/2016/1027/GLN2016102763.pdf'
# url = 'http://www.hkexnews.hk/listedco/listconews/GEM/2016/1027/GLN2016102763.pdf'

a, num = re.subn(r'\d+\.\d+\.\d+\.\d+\/', '', url)
# 如果没有返回
print(a)
print(num)

# with codecs.open('aaa.pdf', 'a', 'utf-8') as file:
#     file.writelines(res)