# -*- coding: utf-8 -*-
import scrapy



class G1Spider(scrapy.Spider):
    name = 'g1'
    allowed_domains = ['g1.globo.com']
    start_urls = ['http://g1.globo.com/']

    def parse(self, response):
        noticias = response.xpath('//a[@class="feed-post-link gui-color-primary gui-color-hover"]/text()').extract()

        x = yield {
            'noticia1': noticias[0],
            'noticia2': noticias[1],
            'noticia3': noticias[2]
            }

        return x
