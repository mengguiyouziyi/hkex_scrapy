#coding:utf-8
import requests
import codecs

url = 'http://www.hkexnews.hk/listedco/listconews/mainindex/SEHK_LISTEDCO_DATETIME_TODAY.HTM'
res = requests.get(url).content.decode()

with codecs.open('aaa.html', 'a', 'utf-8') as file:
    file.writelines(res)
