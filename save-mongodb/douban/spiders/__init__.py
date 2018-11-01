# coding: utf-8

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from douban.items import MusicItem, MusicReviewItem
from scrapy import log

import re

class ReviewSpider(CrawlSpider):
    name = 'douban_music'
    allowed_domains = ['music.douban.com']
    start_urls = ['https://music.douban.com/subject/1406522/']
    rules = (
        # follow=False(不跟进), 只提取首页符合规则的url，然后爬取这些url页面数据，callback解析
        # follow=True(跟进链接), 在次级url页面中继续寻找符合规则的url,如此循环，直到把全站爬取完毕
        # 如果callback参数为None，follow默认设置为True，否则默认为False
        # 多个Rule匹配同一个链接, 只有第一个Rule会被使用
        # 重复的url不会重复访问，但是request_count会增加
        Rule(LinkExtractor(allow="/subject/\d+/reviews$")),
        Rule(LinkExtractor(allow="/subject/\d+/reviews\?start=\d+$")),
        Rule(LinkExtractor(allow="/review/\d+/$"), callback="parse_review"),
    )

    def parse_review(self, response):
        try:
            item = MusicReviewItem()
            # 乐评标题
            item['review_title'] = response.xpath('//*[@property="v:summary"]/text()').extract()
            # 乐评内容
            content = "".join(
                response.xpath('//*[@id="link-report"]/div[@property="v:description"]/text()').extract())
            item['review_content'] = content.lstrip().rstrip().replace("\n", " ")
            # 乐评作者
            item['review_author'] = response.xpath('//*[@property = "v:reviewer"]/text()').extract()
            # 乐评音乐
            item['review_music'] = response.xpath('//*[@class="main-hd"]/a[2]/text()').extract()
            # 乐评时间
            item['review_time'] = response.xpath('//*[@class="main-hd"]/p/text()').extract()
            # 乐评url
            item['review_url'] = response.url
            yield item
        except Exception as error:
            log(error)