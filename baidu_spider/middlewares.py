# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import requests
import lxml
import random
import os
from scrapy import signals

from baidu_spider.config import USER_AGENT, DOMAIN, BLACK_DOMAIN, URL_SEARCH, URL_NEXT, URL_NUM


class BaiduSpiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BaiduSpiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        ua= {'user-agent': self.get_random_user_agent()}
        request.headers.setdefault('User-Agent',self.get_random_user_agent())
        print("header--------------")
        print(request.headers)
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
    
    def get_random_user_agent(self):
        return random.choice(self.get_data('user_agents.txt', USER_AGENT))
    
    def get_data(self, filename, default=''):
        root_folder = os.path.dirname(__file__)
        print("path--------------")
        print(root_folder)
        user_agents_file = os.path.join(
            os.path.join(root_folder, 'spiders/data'), filename)
        try:
            with open(user_agents_file) as fp:
                data = [_.strip() for _ in fp.readlines()]
        except:
            data = [default]
        return data

class ProxyMiddleware(object):

    def get_proxy(self):
        try:
            response = requests.get('http://127.0.0.1:5010/get')
            print(response.text)
            if response.status_code == 200:
                return response.text
            return None
        except ConnectionError:
            return None

    def get_proxy_val(self):
        p = self.get_proxy()
        while p is None:
            p = self.get_proxy()
        proxies = {
            "http" : "http://" + p,
            "https" : "http://{}".format(p)
        }
        return proxies

    def process_request(self,request,spider):
        request.meta['proxy'] = 'http://'+self.get_proxy()
        return None
