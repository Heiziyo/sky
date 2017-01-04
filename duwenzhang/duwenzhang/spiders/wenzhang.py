# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import log
from duwenzhang.items import DuwenzhangItem
from scrapy.selector import Selector
from scrapy.http import Request
class WenzhangSpider(CrawlSpider):
    name = "wenzhang"
    allowed_domains = ["www.duwenzhang.com"]
    start_urls = (
        'http://www.duwenzhang.com/',
    )
    rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        #Rule(LinkExtractor(deny=('http:\/\/www.duwenzhang.com/wenzhang\/.*?\d*',))),
        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('http://www.duwenzhang.com/wenzhang/.*?',),deny='http://www.duwenzhang.com/wenzhang/.*?/.*?/'), callback='parse_item'),
    )
    def parse_item(self, response):
        print "parse_item>>>>>>"
        items = []
        selector = Selector(response)
        links = selector.css('table.tbspan')
        for link  in links:
            item = DuwenzhangItem()
            item['title'] = link.xpath('//b/a[@href]/text()').extract()
            url =  item['url'] = link.xpath('//b/a/@href').extract()
        #yield Request(self.parse_details,meta={'item': item})
        print "end>>>>>>"

    def parse_details(self, response):
        item = response.meta['item']
        # populate more `item` fields
        item['content'] = 1
        return item
