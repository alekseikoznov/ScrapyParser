import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        peps = response.xpath('//section[@id="numerical-index"]').css(
            'tbody').css('tr')
        for pep in peps:
            number, name = pep.css('a.pep::text').getall()
            item = PepParseItem(number=number, name=name)
            pep_link = pep.css('a.pep::attr(href)').get()
            yield response.follow(pep_link, callback=self.parse_pep,
                                  cb_kwargs=dict(item=item))

    def parse_pep(self, response, item):
        status = response.css(
            'dt:contains("Status") + dd').css('abbr::text').get()
        item['status'] = status
        yield item
