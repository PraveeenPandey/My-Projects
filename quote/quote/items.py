# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuoteItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    short_des = scrapy.Field()
    des = scrapy.Field()
    key_skills = scrapy.Field()
    eligibility = scrapy.Field()
    Syll = scrapy.Field()
    amount = scrapy.Field()

