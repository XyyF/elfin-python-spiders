# coding: utf-8

BOT_NAME = 'music'
SCRAPY_NAME = 'music'
SPIDER_MODULES = ['music.spiders']
NEWSPIDER_MODULE = 'music.spiders'
# 爬取深度
# DEPTH_LIMIT = 4
# 延时
DOWNLOAD_DELAY = 2
# chrome://version/  查看用户代理设置
# USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '__remember_me=true; _ntes_nnid=d307668ddf25dbdb8ea8509b2ee062b6,1540694970839; _ntes_nuid=d307668ddf25dbdb8ea8509b2ee062b6; __f_=1540978367628; _iuqxldmzr_=32; __utmc=94650624; WM_TID=7GgWQpJyNSJEVEBFBQMtePg%2Bg4fpk%2Fny; __utmz=94650624.1541643998.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); WM_NI=Ie1n3j1lG9%2FCcDT%2Bbk2n6JJMtKoPb2cUuGE06wIAFPtqCCJzflolAJQjodygcpfGGmsFTeYpaHfRl0JGG50cdxe%2BhGIuoxdLNkUEvfsqnD9f2wrvWZwAvl%2BrWE7yuODMMWU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee84e43bf68da2abf763a5b48eb6d85b969b8faaf36e8deb89b8d744818de18ce22af0fea7c3b92a8bbbff8fb262f3b489daae49a19c9ccce161f2b2faabc947b895a1b1e13aa18bbba8c83cf6a987a2c55cb8af8da4c972a6b4a18dc44293b6a185fc6da1b0aaa8c667b19a9c86dc7ca398aab3ef3c8a9989d6b369a8a8abcceb4d8baba199e7488eb59ba6f56eb1afa2a5bc6ef2a9be97d652b59fba8daa7a959bf99af845889383b8d837e2a3; JSESSIONID-WYYY=2x8QkhJ%2BNY9Udk8Vg1cXlz8%5CpIZca3e7E8zfZupRSG06mZ%5Cf4Q4iJ1HHEGZ%2FCQ1SBt2AK3X%2BXBmwm7vwrtxvUdGqMMzgmQz82Aj4EAVeQ3%2BRDWTreTOCVNUQ%2FdOsG7V7PZeGjDR9Ch49%2Fnx4H%2BJRjNUPfNib8BC5UQGm44X8O651MPIs%3A1541658860279; __utma=94650624.945554872.1541483916.1541646892.1541657686.4; MUSIC_U=c8eaed34245be92a4da44ada831e27198574c5c9481f0f69199704a9b0655115c133d41f85ad8951993a9a2cc80f051e2e47b9a06a51764e617e5a44d0eb2747b1367c1261f01246bf122d59fa1ed6a2; __csrf=c5101bcede96d9bde78b28c808bfe0bc; __utmb=94650624.6.10.1541657686',
    'Host': 'music.163.com',
    'Pragma': 'no-cache',
    'Referer': 'https://music.163.com/',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

ROBOTSTXT_OBEY = True
FEED_EXPORT_ENCODING = 'utf-8'

# mongodb数据库配置
MONGO_HOST = "localhost"  # 主机IP
MONGO_PORT = 25916  # 端口号
MONGO_DB = "test_python"  # 库名
MONGO_COLL = "music"  # collection名

# 项目中pipeline的路径及其启动顺序，会对每一个item在pipeline中执行
ITEM_PIPELINES = {'music.pipelines.musicPipeline': 300}

# 豆瓣乐评内容配置
ALLOWED_DOMAINS = "music.163.com"
BASE_URL = "https://music.163.com/#/djradio?id=2591010"