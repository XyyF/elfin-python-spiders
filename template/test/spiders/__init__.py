# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from lxml import etree
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = 'myspider'

    def start_requests(self):
        return [scrapy.FormRequest("https://xiaojing0.com/workbench_api/manager/signin",
            formdata={'userName': 'Noah', 'password': '33a1cd102fe76c63411cd97bc6be59ab'},
            callback=self.logged_in)]

    def logged_in(self, response):
        print 1311
        print response.headers
        yield scrapy.Request("https://xiaojing0.com/workbench_api/student/multi",
            callback=self.students,
            headers=response.headers,
            method="GET")

    def students(self, response):
        print 123
        print response.body