# coding: utf-8

import scrapy
from tutorial.items import DmozItem
from scrapy.linkextractors import LinkExtractor

class DmozSpider(scrapy.Spider):
    name = "dmoz1"
    allowed_domains = ["music.163.com"]
    start_urls = [
        "https://music.163.com"
    ]
    # /#/djradio?id=2591010
    # link_extractor = LinkExtractor(allow='/program?id=2057712793')

    def start_requests(self):
        url = 'https://music.163.com/djradio?id=2591010'
        yield scrapy.Request(url, callback=self.parse_index)


    def parse_index(self, response):
        # links = self.link_extractor.extract_links(response) #爬取链接
        print response.text[0:5000]