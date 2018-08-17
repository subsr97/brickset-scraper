import scrapy
from datetime import datetime

class BrickSetScraper(scrapy.Spider):
    name = 'brickset_spider'
    start_urls = []

    CURRENT_YEAR = datetime.date(datetime.now()).year
    START_YEAR = CURRENT_YEAR - 5
    END_YEAR = CURRENT_YEAR

    for year in range(START_YEAR, END_YEAR+1):
        start_urls.append("https://brickset.com/sets/year-"+str(year))

    def parse(self, response):
        SET_SELECTOR = '.set'
        NAME_SELECTOR = 'h1 ::text'
        IMG_SELECTOR = 'img ::attr(src)'
        PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
        MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'

        for brickset in response.css(SET_SELECTOR):
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'image': brickset.css(IMG_SELECTOR).extract_first(),
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
            }
        
        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()

        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )