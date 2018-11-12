# coding: utf-8

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from music.items import MusicReviewItem
from scrapy.conf import settings
from scrapy import log

import re

class ReviewSpider(CrawlSpider):
    name = settings['SCRAPY_NAME']
    allowed_domains = [settings['ALLOWED_DOMAINS']]
    start_urls = [settings['BASE_URL']]

    rules = (
        # follow=False(不跟进), 只提取首页符合规则的url，然后爬取这些url页面数据，callback解析
        # follow=True(跟进链接), 在次级url页面中继续寻找符合规则的url,如此循环，直到把全站爬取完毕
        # 如果callback参数为None，follow默认设置为True，否则默认为False
        # 多个Rule匹配同一个链接, 只有第一个Rule会被使用
        # 重复的url不会重复访问，但是request_count会增加
        # Rule(LinkExtractor(allow="/djradio?id=2591010&order=1&_hash=programlist&limit=100&offset=\d+$")),
        Rule(LinkExtractor(allow="/program?id=\d+$"), callback="parse_review"),
    )
    def parse_start_url(self):
        url = 'https://music.163.com/djradio?id=2591010'
        yield scrapy.Request(url, callback=self.parse_index)

    def parse_index(self, response):
        print 12312312
        try:
            item = MusicReviewItem()
            # ID值 music_id
            musicId = response.xpath('//span[@class="u-outlink"]/a[@class="s-fc7"]/@href').extract()
            item['music_id'] = re.findall('(\d+)/$', musicId)

            # 排序值 music_number
            musicNum = response.xpath('//strong[@class="f-fs1"]/text()').extract()
            item['music_number'] = re.findall('\d+', musicNum)

            # 音乐名 music_name
            item['music_number'] = response.xpath('//h2[@class="f-ff2"]/text()').extract()

            # 音乐url
            item['review_url'] = response.url
            yield item
        except Exception as error:
            log(error)