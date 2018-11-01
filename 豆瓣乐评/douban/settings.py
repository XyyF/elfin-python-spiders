# coding: utf-8

BOT_NAME = 'douban'
SCRAPY_NAME = 'douban_music'
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

# mongodb数据库配置
MONGO_HOST = "localhost"  # 主机IP
MONGO_PORT = 25916  # 端口号
MONGO_DB = "test_python"  # 库名
MONGO_COLL = "douban-music"  # collection名

# 项目中pipeline的路径及其启动顺序，会对每一个item在pipeline中执行
ITEM_PIPELINES = {'douban.pipelines.doubanPipeline': 300}

# 豆瓣乐评内容配置
ALLOWED_DOMAINS = "music.douban.com"
BASE_URL = "https://music.douban.com/subject/1406522/reviews"
SUBJECT_ID = "1406522"