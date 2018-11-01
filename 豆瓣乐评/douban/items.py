# coding: utf-8

from scrapy import Item, Field

# 乐评
class MusicReviewItem(Item):
    review_id = Field()
    review_title = Field()
    review_content = Field()
    review_author = Field()
    review_music = Field()
    review_time = Field()
    review_url = Field()