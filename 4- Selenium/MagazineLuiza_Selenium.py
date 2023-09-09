from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

navegador = webdriver.Firefox()
navegador.get("https://www.magazineluiza.com.br/")
navegador.implicitly_wait(10)
input_place = navegador.find_element(By.ID, 'input-search')
input_place.send_keys("geladeira")
input_place.submit()
sleep(5)

produtos = navegador.find_elements(By.CLASS_NAME, 'gjCMbP')
produtos_list = list()

for item in produtos:
    nome = ''
    preco = ''
    link = ''

    if nome == '':
        try:
            nome = item.find_element(By.CLASS_NAME, 'sc-ijtseF').text

        except Exception:
            pass

    elif nome == '':
        try:
            nome = item.find_element(By.CLASS_NAME, 'ypydh').text
        except Exception:
            pass
#------------------------------------------------------------------------------
    if preco == '':
        #sc-kpDqfm eCPtRw sc-eXsaLi buBXNy
        try:
            preco = item.find_element(By.CLASS_NAME, 'sc-kpDqfm').text

        except Exception:
            pass
    elif preco == '':
        try:
            nome = item.find_element(By.CLASS_NAME, 'eCPtRw').text
        except Exception:
            pass
    elif preco == '':
        try:
            nome = item.find_element(By.CLASS_NAME, 'sc-eXsaLi').text
        except Exception:
            pass
    elif preco == '':
        try:
            nome = item.find_element(By.CLASS_NAME, 'buBXNy').text
        except Exception:
            pass
    else:
        preco = '0'
#-------------------------------------------------------------------------------
    if link == '':
        try:
            link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
        except Exception:
            pass
    else:
        link = '-'
    produtos_list.append([nome, preco, link])

import pandas as pd
produtos_df = pd.DataFrame(produtos_list, columns=['Nome', "Preço", "Link"])
print(produtos_df)

produtos_df.to_csv("Produtos_Magazine.csv")
