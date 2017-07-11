# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WikiBotItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    logo = scrapy.Field()
    nasdaq = scrapy.Field()
    wikipedia = scrapy.Field()

class NewsBotItem(scrapy.Item):
    # define the fields for your item here like:
    headline_text = scrapy.Field()
    headline_link = scrapy.Field()
    date = scrapy.Field()
    company = scrapy.Field()
