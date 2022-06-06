import scrapy

class ApartmentSpider(scrapy.spider):
    name = "lab18"
    allowed_domains = ['craigslist.org']
    start_urls = ['https://vermont.craigslist.org/search/apa?search_distance=10&postal=05404&availabilityMode=0&sale_date=all+dates']

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()

        print(titles)

    