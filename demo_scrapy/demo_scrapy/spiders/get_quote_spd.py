import scrapy
from demo_scrapy.items import Quotes

class GetQuoteSpider(scrapy.Spider):
	name = 'lab_get_quote'
	allowed_domains = ['web']
	start_urls = ['http://quotes.toscrape.com/']

   
	def parse(self, response):
   # tiến hành crawl những item đã define trong DemoScrapyItem()
		item = Quotes()
		contents = response.xpath(
            '/html/body/div/div[2]/div[1]/div/span[1]/text()'
				).getall()
		authors = response.xpath(
            '/html/body/div/div[2]/div[1]/div/span[2]/small[1]/text()'
				).getall()

		tags = response.xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/a/text()'
				).getall()

		print('all tags =',tags)
		for i in range(len(contents)):
			item['content'] = contents[i]
			item['author'] = authors[i]
			item['tag'] = tags[i]
			yield item