from selenium import webdriver
import requests
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

opcoes = Options()
opcoes.add_argument('window-size = 400,800')
#opcoes.add_argument('--headless') #faz tudo mas o navegador nao abre
navegador = webdriver.Firefox(options=opcoes)
navegador.get("https://rpachallengeocr.azurewebsites.net/")
navegador.implicitly_wait(10) #pode ser feito com o sleep
#espero 10 segundos para carregar a página
Elementos_Tabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')
linhas = Elementos_Tabela.find_elements(By.TAG_NAME, 'tr')
colunas = Elementos_Tabela.find_elements(By.TAG_NAME, 'td')
for linhaAtual in linhas:
    print(f"{linhaAtual.text}")
