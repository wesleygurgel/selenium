from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import ctypes
import time


def bater_ponto():
    texto_input = driver.find_element(By.ID, 'RegistraPonto')
    print(texto_input.get_attribute('value'))
    if texto_input.get_attribute('value') == "  REGISTRAR ENTRADA  ":
        texto_input.click()


def verificar_ponto():
    driver.refresh()
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,750)", "")
    texto_input = driver.find_element(By.ID, 'RegistraPonto')

    if texto_input.get_attribute('value') == "  REGISTRAR ENTRADA  ":
        texto_input.click()
        return 1
    return 2


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://intranet.trt21.local/default.asp")
time.sleep(1)
driver.maximize_window()

try:
    driver.find_element(By.XPATH, '//a[@href="/asp/pel2/Inicio.asp"]').click()
    driver.execute_script("window.scrollBy(0,750)", "")

except:
    ctypes.windll.user32.MessageBoxW(0, "Provavelmente você não está logado na intra com o Google Chrome",
                                     "ERROR", 1)

verify = 2
contador = 1
while verify == 2:
    if contador >= 3:
        break
    bater_ponto()
    verify = verificar_ponto()
    contador += 1

ctypes.windll.user32.MessageBoxW(0, "Ponto Batido com Sucesso\nPode ir tomar seu cafezinho meu jovem",
                                 "Ponto Eletrônico", 1)
driver.close()
