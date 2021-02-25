import datetime
import getpass

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
    try:
        texto_input = driver.find_element(By.ID, 'RegistraPonto')
    except:
        if driver.find_element(By.XPATH, "//*[contains(text(), 'permitido para registro do ponto.')]"):
            ctypes.windll.user32.MessageBoxW(0, f"Amigo, ainda faltam {checar_hora()} minutos para o senhor bater o ponto\nEspere com o programa aberto, por favor!",
                                             "Antes do horário permitido", 0)
            tempo_espera = (checar_hora() * 60)
            print(f'Tempo de espera definido para: {tempo_espera} segundos')
            time.sleep(tempo_espera)
            verificar_ponto()


    if texto_input.get_attribute('value') == "  REGISTRAR ENTRADA  ":
        texto_input.click()
        return 1
    return 2


def data_hoje():
    data = datetime.datetime.now()
    dia_atual = data.day
    mes_atual = data.month
    ano_atual = data.year

    return f'{dia_atual}-{mes_atual}-{ano_atual}'

def checar_hora():
    formato = '%H:%M'
    atual = datetime.now()
    atual = atual.strftime('%H:%M')
    horario_esperado = '07:20'

    data1 = datetime.strptime(atual, formato)
    data2 = datetime.strptime(horario_esperado, formato)

    diff = data2 - data1
    diff_minutes = (diff.days * 24 * 60) + (diff.seconds / 60)
    return diff_minutes


# INICIO DO CODIGO ---------------

# CRIANDO MEU LOG FILE
username = getpass.getuser()
data_atual = data_hoje()
log_file = open(f'{data_atual}.log', 'a')

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://intranet.trt21.local/default.asp")
time.sleep(1)
driver.maximize_window()

try:
    driver.find_element(By.XPATH, '//a[@href="/asp/pel2/Inicio.asp"]').click()
    driver.execute_script("window.scrollBy(0,750)", "")

except:
    log_file.write(f'Algum problema aconteceu ao tentar bater o ponto para {username.upper()}')
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

log_file.write(f'Ponto batido as {datetime.datetime.now()}\nUSUARIO: {username.upper()}')
ctypes.windll.user32.MessageBoxW(0, "Ponto Batido com Sucesso\nPode ir tomar seu cafezinho meu jovem",
                                 "Ponto Eletrônico", 0)
driver.close()
log_file.close()
exit(1)
