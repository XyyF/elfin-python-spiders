# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from lxml import etree
from scrapy.conf import settings
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = settings['SCRAPY_NAME']
    allowed_domains = [settings['ALLOWED_DOMAINS']]
    start_urls = [settings['BASE_URL']]
    rules = (
        # follow=False(不跟进), 只提取首页符合规则的url，然后爬取这些url页面数据，callback解析
        # follow=True(跟进链接), 在次级url页面中继续寻找符合规则的url,如此循环，直到把全站爬取完毕
        # 如果callback参数为None，follow默认设置为True，否则默认为False
        # 多个Rule匹配同一个链接, 只有第一个Rule会被使用
        # 重复的url不会重复访问，但是request_count会增加
        Rule(LinkExtractor(allow="/yirenzhixia/248016.html?p=\d+$"), callback="parse_review"),
    )

    def parse_review(self, response):
        # https://manga.mipcdn.com/i/s/https://mhimg.eshanyao.com/ManHuaKu/y/yirenzhixia/1jiejie1/2019300523.jpg
        try:
            item = DmozItem()
            # 图片链接
            item['link'] = response.xpath('//div[@id="images"]/image/@src').extract()
            yield item
        except Exception as error:
            log(error)