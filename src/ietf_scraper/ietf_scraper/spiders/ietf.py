import scrapy


class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        title = response.xpath("//span[@class=title]/text()").get()
        return {"title": title}
