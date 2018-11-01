# coding:utf-8

from scrapy import cmdline
# cmdline.execute("scrapy crawl douban_music -o item.json".split())
cmdline.execute("scrapy crawl douban_music".split())