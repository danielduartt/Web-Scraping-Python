import requests
from bs4 import BeautifulSoup

response = requests.get("https://g1.globo.com/")
print(f"Status Code: {response.status_code}")
print("==============================================================================")
print(type(response.content))
content = response.content #conteudo html
#Vamos converter essa variável "content" para o tipo BeatifulSoup
site = BeautifulSoup(content, 'html.parser') #Instanciando um obj da classe BeatifulSoup
print(type(site))
#print(site.prettify()) #imprime o site de forma organizada
print("Buscando uma notícia")
post = site.find("div", attrs = {'class': 'feed-post-body'})
print(post.prettify())

'''
Resumo: 
    
    response = resquest.get("link")
    response.status_code
    content = response.content
    
    site = BeautifulSoup(variável, "tipodela.parser"
    site.prettyfy() => mostrar de forma organizada o código html 
    
    noticia = site.find("tipo da tag", attrs = {"(especificação)class" : "nome dado da class"}) 
    usa-se o método find para procurar um dado elemento no html, pegando seu dado 
    
'''
