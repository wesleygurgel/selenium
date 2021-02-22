import getpass
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

# CRIANDO MEU LOG FILE
username = getpass.getuser()
log_file = open(f'bbb.log', 'a')

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://gshow.globo.com/realities/bbb/bbb21/votacao/paredao-bbb21-vote-para-eliminar-arthur-gilberto-ou-karol-conka-838ec4d5-7d17-4263-a335-29e13c3a769b.ghtml")
time.sleep(1)
driver.maximize_window()

# a = driver.find_element(By.XPATH, '//div[@class="_f7162a1a2439270341c"]').text
a = driver.find_element(By.XPATH, '//*[text()="Karol Conká"]')
print(a.text)
print(a)
print(a.id)



# try:
#     driver.execute_script("window.scrollBy(0,750)", "")
#
# except:
#     log_file.write(f'Algum problema aconteceu ao tentar bater o ponto para {username.upper()}')
#     ctypes.windll.user32.MessageBoxW(0, "Provavelmente você não está logado na intra com o Google Chrome",
#                                      "ERROR", 1)
#
# verify = 2
# contador = 1
# while verify == 2:
#     if contador >= 3:
#         break
#     bater_ponto()
#     verify = verificar_ponto()
#     contador += 1
#
# log_file.write(f'Ponto batido as {datetime.datetime.now()}\nUSUARIO: {username.upper()}')
# ctypes.windll.user32.MessageBoxW(0, "Ponto Batido com Sucesso\nPode ir tomar seu cafezinho meu jovem",
#                                  "Ponto Eletrônico", 1)
# driver.close()
# log_file.close()
# exit(1)