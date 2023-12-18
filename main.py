from selenium import webdriver  # pip install selenium
from selenium.webdriver.common.by import By  # Importar o By
from selenium.webdriver.common.keys import Keys as keys  # Importar o Keys

driver = webdriver.Chrome()  # Instanciar o objeto webdriver

driver.get("https://www.google.com")  # Abrir o site

# Encontrar o elemento pelo xpath
search = driver.find_element(By.XPATH,
                             '//*[@id="APjFqb"]')

# Enviar as teclas para o elemento
search.send_keys('Python' + keys.ENTER)

# Encontrar o elemento pelo xpath
result = driver.find_element(By.XPATH,
                             '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div/div[1]/div/div/div')

print(result.text)  # Imprimir o texto do elemento

driver.quit()  # Fechar o navegado