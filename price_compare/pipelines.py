from scrapy import Item, Spider


class Pipeline:
    def process_item(self, item: Item, spider: Spider) -> Item:
        return item
