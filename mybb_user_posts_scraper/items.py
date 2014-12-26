# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Post(scrapy.Item):
    title = scrapy.Field()
    post_id = scrapy.Field()
    link = scrapy.Field()
    text = scrapy.Field()
    date_posted = scrapy.Field()

class Author(scrapy.Item):
    username = scrapy.Field()
    profile_link = scrapy.Field()