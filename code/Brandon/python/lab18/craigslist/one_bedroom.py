import scrapy


class ApartmentsSpider(scrapy.Spider):
    name = 'one_bedroom'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://vermont.craigslist.org/search/burlington-vt/one-bedroom-apartment?sort=date&lat=44.4735&lon=-73.1845&search_distance=6.6']


    def parse(self, response):
        titles = response.xpath('//div[@class="result-info"]')
        
        for x in titles:
            name = x.xpath('.//a/text()').extract_first()
            date = x.xpath('.//time[@class="result-date"]/text()').extract_first()
            price = x.xpath('.//span[@class="result-price"]/text()').extract_first("0")
            location = x.xpath('.//span[@class="result-hood"]/text()').extract_first("na")
            yield{
                'Date' : date,
                'Price' : price,
                'Name' : name,
                'Location' : location,
            }

# process = CrawlerProcess(settings={
#     "FEEDS": {
#         "items.json": {"format": "json"},
#     }
# })            

# process.crawl(ApartmentsSpider)
# process.start()
    # def parse(self, response):
    #     titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
    #     print(titles)
