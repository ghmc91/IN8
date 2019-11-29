import requests
import re

to_crawl =['http://www.g1.globo.com'] #url para fazer o crawler (a semente: ponto de partida)
crawled = set()# o conjunto do que "ja fiz"/ja percorrido, foi feito o crawer
#se a url já estiver em crawled, vou para a próxima!

#é bom usar header pra finger ser um navegador
header = {"user-agent":"Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0",
          "accept": "*/*",
          "accept-language": "en-US,en;q=0.5",
          "accept-encoding": "gzip, deflate",
          "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
          }
while True: #executar pra sempre...

    url = to_crawl[0]
    try: #tratar pox ex URL invalidas..
        req = requests.get(url,headers=header)
    except: #remove a url
        to_crawl.remove(url)
        crawled.add(url)
        continue #passa pro prox link


    #print (req.text) #é a página!
    html = req.text



    links = re.findall(r'(?<=href=["\'])https?://.+?(?=["\'])' ,html)
    print ("Crawling", url)

    #apos a requisicao, removo do to_crawl e insiro em no conjunto crawled:
    to_crawl.remove(url)
    crawled.add(url)


    #agora joga links in to_crawl se nao estiverem em crawled:
    for link in links:
        if link not in crawled and link not in to_crawl:  #se nao estiver nas 2 listas
            to_crawl.append(link)


    #print(padrao.group())
    #print(padrao,)

    for link in links:
        print(link)