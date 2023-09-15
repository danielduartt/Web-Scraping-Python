import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/page/1/',
                  'https://quotes.toscrape.com/page/2/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                "text": quote.css('span.text::text').get(),
                "author": quote.css('small.author::text').get(),
                "tag": quote.css('div.tags a.tag::text').getall()
            }


#scrapy crawl (nome dado a spider)
#scape crawl -o quotes.json
