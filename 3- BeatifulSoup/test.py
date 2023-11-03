import requests
from bs4 import BeautifulSoup

url_pagina_principal = 'https://www.cbf.com.br/futebol-brasileiro/atletas/campeonato-brasileiro-serie-b/2022/20056'

response = requests.get(url_pagina_principal)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    jogadores = soup.find_all('th', attrs={'scope': 'row'})
    link_jogador = list()

    for jogador in jogadores:
        href = jogador.find('a', href=True)
        link_jogador.append(href['href'])

    for link in link_jogador:
        reponse_jogador = requests.get(link)
        if reponse_jogador.status_code == 200:
            soup_jogador = BeautifulSoup(reponse_jogador.text, 'html.parser')

            nome_jogador = soup_jogador.find("span", attrs={"class": "nome_completo"}).text
            valores_jogador = soup_jogador.find_all("span", attrs={'class', 'valor'})
            idade_jogador = valores_jogador[0].text
            nasc_jogador = valores_jogador[1].text
            print(f"Nome: {nome_jogador}")
            print(f"Idade: {idade_jogador}")
            print(f"Data de nascimento: {nasc_jogador}")
            print("-------------------------------------------")