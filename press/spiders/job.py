import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class JobSpider(CrawlSpider):
    name = 'job'
    allowed_domains = ['medicalxpress.com']
    start_urls = ['https://medicalxpress.com/archive/2-11-2020/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[@class="selection-article__description"]/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//li[@class="page-item"]/a'), follow=True)
    )

    def parse_item(self, response):
        title = response.xpath('//h1/text()').get()
        doi = response.xpath('//*[@class="article-main__more p-4"]/a/text()').get()
        provided_by = response.xpath('//*[@class="d-inline-block text-medium my-4"]/a[1]/text()').get()
        url = response.url
        yield{
            'Title': title,
            'Doi': doi,
            'Provided_by': provided_by,
            'Url': url
        }