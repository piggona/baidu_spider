# -*- coding: utf-8 -*-

# Scrapy settings for baidu_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

BOT_NAME = 'baidu_spider'

SPIDER_MODULES = ['baidu_spider.spiders']
NEWSPIDER_MODULE = 'baidu_spider.spiders'

MONGO_URI='localhost'
MONGO_DB='baidu_spider'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'baidu_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
def getCookie():
    cookie_list = [
        'CGIC=InZ0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIy; SID=KAcnFMvInhK_kR_30d2ZE_RbfL_l58e99RAbVp2xO1u6PQ3YzVbl8De3NTWAIDfWtIKDXA.; HSID=A3sCm-Fdp9cPHR_KQ; SSID=AuPB-d1fhYJOpjQf_; APISID=47vLNvMei34IWHST/AqixuPTAu9n4fP0qL; SAPISID=e80Ny2ft_zyWIA-I/AJfAaY24gnK0qDm9c; NID=162=KjSR39oPEquVsXEtsKa2sst1gKCMbhw8HoSEUVHhxLFl4-bdMMawUOEprmBZgqmW8Dh-xvnSJCd2W713Pne8SO_ZRWTyzVdUxiwt-hA2FakhC4OPJJgp67LOE4MrbqPAw-ZB7FswA0a3hUM0Z1avNtMsTZhjDx8-kGbbShu2BWm-_S4qrQJqEIxMkDDYyjTPVbqFt4XtDh4ZMWTzB0jGrq2qUjJ7bSI8i_Bctuz3F4ZjyAJB5m5jm1j-; 1P_JAR=2019-03-08-00; UULE=a+cm9sZToxIHByb2R1Y2VyOjEyIHByb3ZlbmFuY2U6NiB0aW1lc3RhbXA6MTU1MjAwNTU1ODIwMTAwMCBsYXRsbmd7bGF0aXR1ZGVfZTc6Mzk5NjM2NDQ5IGxvbmdpdHVkZV9lNzoxMTYzNTA2MzUwfSByYWRpdXM6NDU4ODA=; SIDCC=AN0-TYtdfF85AH68n932zmNof-h2I88iKtbW_PqqnNW28lRxYP7ZHANCUd-6MqsgKxix2kW_CQ'
    ]
    cookie = random.choice(cookie_list)
    return cookie

DEFAULT_REQUEST_HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b2",
    'Accept-Language': "zh-CN,zh;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Connection":"keep-alive",
    "Host":"www.baidu.com",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    'Upgrade-Insecure-Requests':'1',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'%s' % getCookie()
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'baidu_spider.middlewares.BaiduSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'baidu_spider.middlewares.BaiduSpiderDownloaderMiddleware': 543,
   'baidu_spider.middlewares.ProxyMiddleware':400
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'baidu_spider.pipelines.BaiduSpiderPipeline': 300,
   'baidu_spider.pipelines.MongoPipeline': 400
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

'''下载延时，即下载两个页面的等待时间'''
DOWNLOAD_DELAY = 0.5

'''并发最大值'''
CONCURRENT_REQUESTS = 100

'''对单个网站并发最大值'''
CONCURRENT_REQUESTS_PER_DOMAIN = 100

'''启用AutoThrottle扩展，默认为False'''
AUTOTHROTTLE_ENABLED = False

'''设置下载超时'''
DOWNLOAD_TIMEOUT = 10

'''降低log级别，取消注释则输出抓取详情'''
# LOG_LEVEL = 'INFO'