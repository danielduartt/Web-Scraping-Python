
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://www.mercadolivre.com.br/')
input_search = driver.find_element(By.XPATH, '//*[@id="cb1-edit"]')
input_search.send_keys("Fone hyperx")
input_search.submit()


