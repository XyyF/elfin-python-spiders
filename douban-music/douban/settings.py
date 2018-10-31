# coding: utf-8

BOT_NAME = 'douban'
SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'
# 爬取深度
DEPTH_LIMIT = 4
# 延时
DOWNLOAD_DELAY = 2
# chrome://version/  查看用户代理设置
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
ROBOTSTXT_OBEY = True
FEED_EXPORT_ENCODING = 'utf-8'