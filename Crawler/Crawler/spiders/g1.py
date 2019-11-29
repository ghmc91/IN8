# -*- coding: utf-8 -*-
import scrapy
import json



class G1Spider(scrapy.Spider):
    name = 'g1'
    allowed_domains = ['g1.globo.com']
    start_urls = ['http://g1.globo.com/']

    def parse(self, response):
        noticias = response.xpath('//div[@class="feed-post-body"]/div[@class="feed-post-body-title gui-color-primary gui-color-hover "]//a[@class="feed-post-link gui-color-primary gui-color-hover"]/text()').extract()
        subtitulo = response.xpath('//div[@class="feed-post-body"]/div[@class="feed-post-body-resumo"]/div[@class="_label_event"]/text()').extract()

        noticias_dict = {
            'Página':{
            'url': response.url},
            'Notícia 1' : {
            'Título': noticias[0],
            'Subtítulo':subtitulo[0]},
            'Notícia 2' : {
            'Título': noticias[1],
            'Subtítulo':subtitulo[1]},
            'Notícia 3' : {
            'Título': noticias[2],
            'Subtítulo': subtitulo[2]}
            }
        
        with open('noticias.json', 'w', encoding='utf-8') as json_file:
            json.dump(noticias_dict, json_file, ensure_ascii=False)


        
