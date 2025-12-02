import scrapy

class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        for cit in response.xpath('//div[@class="figsco__quote__text"]'):
            text_value = cit.xpath('a/text()').extract_first()
            # Retirer les caractères “ et ” (Unicode 201C et 201D)
            if text_value:
                text_value = text_value.replace("\u201c", "").replace("\u201d", "")
            # XPath pour l'auteur (le plus proche du texte)
            author_value = cit.xpath('../../div[@class="figsco__quote__author"]/a/text()').extract_first()
            # Filtrer uniquement Winston Churchill
            if author_value and "churchill" in author_value.lower():
                yield { 'text': text_value, 'author': author_value }