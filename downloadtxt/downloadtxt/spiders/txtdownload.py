import scrapy
from scrapy.selector import Selector
from downloadtxt.items import DownloadtxtItem


class TxtSpider(scrapy.Spider):
    name = "txter"
    allowed_domains = ['www.58utxt.com']
    start_urls = ['https://www.58utxt.com/read/24437/12666926.html']

    def parse(self, response):
        items = []
        sel = Selector(response)
        content = sel.xpath('//div/div/div[2]/p[1]/text()').extract()
        title = sel.xpath('//h1/text()').extract()
        item = DownloadtxtItem()
        item['title'] = title
        item['Content'] = content
        items.append(item)
        print(type(content))
        content1 = str(content)
        filename = "ss.txt"
        with open(filename, 'w+') as f:
            f.write(content1)

        return items
# scrapy crawl txter -o items.json -t json
