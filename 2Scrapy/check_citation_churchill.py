import scrapy

class CitationsXPathSpider(scrapy.Spider):
    name = "citations_xpath_spider"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        # Utilisation de XPath pour extraire les citations et auteurs
        for idx, quote in enumerate(response.xpath("//div[@class='quote']"), start=1):
            text = quote.xpath(".//span[@class='text']/text()").get()
            author = quote.xpath(".//small[@class='author']/text()").get()
            yield {
                "position": idx,
                "text": text,
                "author": author
            }
        # Pagination : suivre le lien "next" si présent
        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            yield response.follow(next_page, self.parse)
