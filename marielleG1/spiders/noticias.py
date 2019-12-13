import scrapy
import ipdb

class BlogSpider(scrapy.Spider):
    name = "noticias"
    paginas = 1

    def start_requests(self):
        urls = [
            'https://g1.globo.com/tudo-sobre/marielle-franco/'
        ]
        ##for url in urls:
          ##  yield scrapy.Request(url=url, callback=self.parse)
        for i in range(163):
            url = 'https://g1.globo.com/tudo-sobre/marielle-franco/index/feed/pagina-{}.ghtml'.format(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range (9):
            #ipdb.set_trace()
            titulo = response.css('a.feed-post-link ::text')[i].get()
            resumo = response.css('div.feed-post-body-resumo ::text')[i].get()
            print("{")
            print(f"'titulo':'{titulo}' , 'resumo': '{resumo}' ")
            print('}')
            print()
        pass

