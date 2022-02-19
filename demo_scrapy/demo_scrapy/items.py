# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Quotes(scrapy.Item):
	content = scrapy.Field()
	author = scrapy.Field()
	tag = scrapy.Field()

class Catergory_Cpn(scrapy.Item):
	name = scrapy.Field()
	link = scrapy.Field()
	categoryCode = scrapy.Field()

class Product_Cpn(scrapy.Item):
	productName = scrapy.Field()
	price = scrapy.Field()
	storage = scrapy.Field()
	production = scrapy.Field()