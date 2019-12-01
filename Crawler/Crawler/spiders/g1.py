# -*- coding: utf-8 -*-
import scrapy
import json



class G1Spider(scrapy.Spider):
    name = 'g1'
    allowed_domains = ['g1.globo.com']
    start_urls = ['http://g1.globo.com/']

    def parse(self, response):    

        titulo = []
        subtitulo = []
        imagem = []

        for noticia in response.xpath('//div[@class="feed-post-body"]'):        
            titulo.append(noticia.xpath('//a[@class="feed-post-link gui-color-primary gui-color-hover"]/text()').extract())
            if (noticia.xpath('//div[@class="_label_event"]/text()').get() is None):
                subtitulo.append(' ')
            else:
                subtitulo.append(noticia.xpath('//div[@class="feed-post-body-resumo"]//text()').extract())
            if (noticia.xpath('//picture/img/@src').get() is None):
                imagem.append(' ')
            else:
                imagem.append(noticia.xpath('//picture/img/@src').extract()
)
        noticias_dict = {
            'Notícia 1' : {
            'Título': titulo[0][0],
            'Subtítulo':subtitulo[0][0],
            'URL_Imagem': imagem[0][0]},
            'Notícia 2' : {
            'Título': titulo[0][1],
            'Subtítulo':subtitulo[0][1],
            'URL_Imagem': imagem[0][1]},
            'Notícia 3' : {
            'Título': titulo[0][2],
            'Subtítulo':subtitulo[0][2],
            'URL_Imagem': imagem[0][2]}
            }       
        
        with open('noticias.json', 'w', encoding='utf-8') as json_file:
            json.dump(noticias_dict, json_file, ensure_ascii=False)


        
