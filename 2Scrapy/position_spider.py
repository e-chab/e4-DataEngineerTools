import scrapy

class PositionSpider(scrapy.Spider):
    name = "position_spider"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        # Pour chaque citation, on récupère la position (index + 1), le texte et l'auteur
        for idx, quote in enumerate(response.css("div.quote"), start=1):
            yield {
                "position": idx,
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get()
            }
        # Pagination : suivre le lien "next" si présent
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
