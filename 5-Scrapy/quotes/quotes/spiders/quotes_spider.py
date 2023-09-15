import scrapy

def clean_text(text):
    text = text.strip(u'\u201c')
    text = text.strip(u'\u201d')
    return text

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                "text": clean_text(quote.css('span.text::text').get()),
                "author": clean_text(quote.css('small.author::text').get()),
                "tag": quote.css('div.tags a.tag::text').getall()
            }

        next_page = response.css('li.next a::attr(href)').get() #pega os links relativos
        if next_page is not None: #se existir, vai executar o que está dentro do if
            yield response.follow(next_page, callback=self.parse) #callback = a um método de classe






#scrapy crawl (nome dado a spider)
#scape crawl -o quotes.json
#response.css('li.next a::attr(href)').get() pegar o link do href

