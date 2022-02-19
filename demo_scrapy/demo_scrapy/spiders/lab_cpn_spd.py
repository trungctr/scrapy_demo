import scrapy
import pymysql.cursors

gottedfile = open('C:\project\py\lab\demoCrawler\demo_scrapy\demo_scrapy\spiders\cpn.txt','r')
DOMAIN = gottedfile.readline().strip('\n')
URLS= gottedfile.readline().strip('\n')
gottedfile.close()

resultfile = open('C:\project\py\lab\demoCrawler\demo_scrapy\demo_scrapy\spiders\cpnResult.txt','w', encoding="utf-8")
links = []
# connection = pymysql.connect(host='localhost',
#                              user='user',
#                              password='passwd',
#                              database='cpn',
# 										 port = 3306
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

class CpnSpider(scrapy.Spider):
	name = 'lab_cpn'
	allowed_domains = [DOMAIN]
	start_urls = [URLS]

	def parse(self, response):
		categories = response.xpath('//*[@id="nav_main"]/div/div/div[1]/div[2]/div/div')
		resultfile.write('Danh sách nhóm hàng\n')
		count = 1
		for cate in categories:
		# crawl các nhóm hàng của cpn
			n = cate.xpath('./a').attrib['title']
			l = URLS + cate.xpath('./a').attrib['href']
			c = 'cpn'+ str(count)
			cat = [n, l, c]
			links.append(cat)
			resultfile.write('name :'+ n +'\n')
			resultfile.write('link :'+ l +'\n')
			resultfile.write('code :'+ c +'\n')
			count +=1
			# with connection:
			# 	with connection.cursor() as cursor:
			# 		# Create a new record
			# 		sql = "INSERT INTO `categories` (`name`, `link`,`code`) VALUES (%s, %s, %s)"
			# 		cursor.execute(sql, (n, l, c))
			# 		connection.commit()
		resultfile.write('\n')
		for link in links:
			yield scrapy.Request(link[1], callback = self.getProduct)


		# nếu có trang tiếp theo thì xử lý lấy tiếp dữ liệu
		nextpage = response.xpath('//*[@id="CategoryPagingBottom"]/div/div[2]/a/@href').get()
		if nextpage:
			yield scrapy.Request(nextpage, callback = self.parse)

		# connection.close()

	def getProduct(self, response):
		#crawl các sản phẩm có trong nhóm hàng hiện hành

		thisCat = response.xpath('/html/head/title/text()').get()
		resultfile.write('\n---------------------------------------\nNhóm hàng : '+ thisCat +'\n\n')
		products = response.xpath('//*[@id="frmCompare"]/ul/div')
		for product in products:
			name = product.xpath('./div/div[2]/a/text()').get()
			price = product.xpath('./div/div[3]/em/strike/text()').get()
			salePrice = product.xpath('./div/div[3]/em/span/text()').get()
			status = product.xpath('./div/div[3]/div[1]/span/text()').get()
			category = thisCat
			resultfile.write('Name : '+ name +'\n')
			resultfile.write('Price : '+ str(price) +'\n')
			resultfile.write('salePrice : '+ str(salePrice) +'\n')
			resultfile.write('category : '+ category +'\n')
			resultfile.write('status : '+ status +'\n')
			resultfile.write('\n')

			# with connection:
			# 	with connection.cursor() as cursor:
			# 		# Create a new record
			# 		sql = "INSERT INTO `products` (`name`, `price`,`salePrice`,`status`,`category`) VALUES (%s, %s, %s, %s, %s)"
			# 		cursor.execute(sql, (name, price, salePrice, status, category )
			# 		connection.commit()



		
