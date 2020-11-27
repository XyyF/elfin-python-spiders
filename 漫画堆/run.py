# coding:utf-8

# 将内容存取到item.json文件中
from scrapy import cmdline
cmdline.execute("scrapy crawl review -o item.json".split())