# coding: utf-8

from scrapy import Item, Field

# 乐评
class MusicReviewItem(Item):
    music_id = Field()
    music_number = Field()
    music_name = Field()
    music_url = Field()