from pathlib import Path
from scrapy import Spider
from scrapy.http.response.html import HtmlResponse


class BoxLunchSpider(Spider):
    name = "box_lunch"
    start_urls = [
        "https://www.boxlunch.com/product/funko-pop-disney-stitch-as-gus-gus-vinyl-figure-%E2%80%94-boxlunch-exclusive/31290478.html",
        "https://www.boxlunch.com/product/funko-pop-animation-one-piece-kaido-vinyl-figure/31158223.html",
    ]

    def parse(self, response: HtmlResponse):
        is_sale = (
            len(
                response.xpath(
                    './/div[@class="price"]//span[@class="sales default-price"]'
                )
            )
            == 0
        )
        if is_sale:
            sale_price = response.xpath(
                './/div[@class="price"]//span[@class="value"]/text()'
            ).extract_first()

            price = response.xpath(
                './/div[@class="strike-through"]//span[@class"value"]'
            ).extract_first()
        else:
            price = response.xpath(
                './/div@class="price"]//span[@class="sales default-price"]//span@class="value"]/text()'
            ).extract_first()

        data = {
            "productName": response.xpath(
                './/h1[@class="product-name-ada"]/text()'
            ).extract_first(),
            "price": response.xpath(
                './/div[@class="price"]//span[@class="value"]/text()'
            ).extract_first(),
        }

        yield data
