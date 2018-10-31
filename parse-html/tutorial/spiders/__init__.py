# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["scrapy-chs.readthedocs.io"]
    start_urls = [
        "from_crawlerhttps://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/tutorial.html"
    ]

    def parse(self, response):
        result = response.xpath('//p[@class="caption"]/span[@class="caption-text"]/text()').extract()
        for sel in result:
            item = DmozItem()
            item['title'] = sel
            yield item