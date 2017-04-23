# -*- coding: utf-8 -*-
# Scrapy settings for crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'hkex'

SPIDER_MODULES = ['hkex.spiders']
NEWSPIDER_MODULE = 'hkex.spiders'

DOWNLOADER_MIDDLEWARES = {
    'hkex.middlewares.ProxyMiddleware': 100,#代理中间件
    'hkex.middlewares.RotateUserAgentMiddleware': 200,#请求头中间件
    # 'crawler.middlewares.JavaScriptMiddleware': 543,  # 键为中间件类的路径，值为中间件的顺序
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,  # 禁止内置的中间件
}

ITEM_PIPELINES = {
    'hkex.pipelines.MongodbPipeline': 800,
}

#禁用cookies
COOKIES_ENABLES = False

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
#302 Problem
# DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 2  # 间隔时间,两次下载的间隔
# RANDOMIZE_DOWNLOAD_DELAY = True  # 开启随机延迟

USER_AGENT_CHOICES = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
]

LOG_STDOUT = True

LOG_LEVEL = 'INFO'

# REACTOR_THREADPOOL_MAXSIZE = 1

# RETRY_ENABLED: True
# RETRY_TIMES: 3
# RETRY_HTTP_CODECS: [500, 502, 503, 504, 400, 408]
# DOWNLOAD_TIMEOUT = 15

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Host': 'www.hkex.com.hk',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.hkexnews.hk/listedco/listconews/advancedsearch/search_active_main_c.aspx',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    # 'If-Modified-Since': 'Thu, 20 Apr 2017 05:39:20 GMT',
    # 'If-None-Match': '"0f4387598b9d21:0"',
    'Cache-Control': 'max-age=0',
}

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'hkex'
MONGODB_COLECNAME = 'all_url'