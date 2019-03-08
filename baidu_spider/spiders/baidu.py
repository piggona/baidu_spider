# -*- coding: utf-8 -*-
import scrapy
import re
import urllib

from baidu_spider.items import BaiduSpiderItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://cn.bing.com/q=python']

    def __get_url_query(self, url):
        m = re.search("wd=(.*)", url).group(1)
        return m
    def parse(self, response):
        n = 0
        for sel in response.xpath('//td[@class="f"]'):
            query = urllib.unquote(self.__get_url_query(response.url))

            item = BaiduSpiderItem()

            title = re.sub('<[^>]*?>','',sel.xpath('.//a/font[@size="3"]').extract()[0])
            lading = sel.xpath('.//a[1]/@href').extract()[0]
            time = sel.xpath('.//font[@color="#008000"]/text()').re('(\d{4}-\d{1,2}-\d{1,2})')[0]
            size = sel.xpath('.//font[@color="#008000"]/text()').re('(\d+K)')[0]

            n += 1

            item['rank'] = n
            item['title'] = title.encode('utf8')
            item['lading'] = lading.encode('utf8')
            item['time'] = time.encode('utf8')
            item['size'] = size.encode('utf8')
            item['query'] = query

            yield item
