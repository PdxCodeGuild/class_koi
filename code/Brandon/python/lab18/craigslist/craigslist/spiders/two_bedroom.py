import scrapy


class ApartmentsSpider(scrapy.Spider):
    name = 'two_bedroom'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://vermont.craigslist.org/search/burlington-vt/two-bedroom-apartment?lat=44.4735&lon=-73.1845&search_distance=6.6']


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
