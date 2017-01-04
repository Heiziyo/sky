# -*- coding: utf-8 -*-
import scrapy


class LlttSpider(scrapy.Spider):
    name = "lltt"
    allowed_domains = ["loldytt.com"]
    start_urls = ['http://loldytt.com/']

    def parse(self, response):
        pass
