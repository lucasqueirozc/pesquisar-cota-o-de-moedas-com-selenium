from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#colocando o nome do web driver como navegador
navegador = webdriver.Chrome()

#codigo para pesquisar google
navegador.get('https://www.google.com.br/')

#pesquisar o valor do dolar
navegador.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys('cotação dolar')
navegador.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys(Keys.ENTER)

#pegar o valor do dolar e depois mostra aqui
cotacao_dolar = navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)

#clicar no nome do google para ir para a pagina inicial do google
navegador.find_element(By.XPATH, '//*[@id="logo"]/img').click()

#pesquisou a cotação do euro
navegador.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys('cotação euro')
navegador.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys(Keys.ENTER)

#pegar o valor do euro e depois mostra aqui
cotacao_euro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)

navegador.quit()