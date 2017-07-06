# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class KonachanSpider(CrawlSpider):
    name = 'konachan'
    allowed_domains = ['konachan.com']
    # start_urls = ['http://konachan.com/post?tags=short_hair']

    rules = (
        Rule(LinkExtractor(allow=r'/post/show/'),
             callback='parse_image', follow=True),
        Rule(LinkExtractor(allow=r'/post\?page'), follow=True),
    )

    def start_requests(self):
        yield scrapy.Request('http://konachan.com/post?tags=' + self.category)

    def parse_image(self, response):
        src = response.css('#image::attr(src)').extract_first()
        tags = response.css('#image::attr(alt)').extract_first().split()
        rating = re.search('Rating: (\w+) ', response.text)[1]
        score = int(re.search('Score: <.*>(\d+)', response.text)[1])

        yield {
            "image_urls": [response.urljoin(src)],
            "tags": tags,
            "rating": rating,
            "score": score,
        }
