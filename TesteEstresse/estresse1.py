from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path='C:/Users/Wesley/Desktop/selenium/geckodriver.exe')
driver.get("https://sistemas-hml.trt21.jus.br/certidao-web/#/certidao")
time.sleep(2)
driver.maximize_window()

driver.find_element(By.NAME, "inputCpf").send_keys("70383775400")

driver.find_element(By.NAME, "radioArquivados").click()

contador = 0

while contador < 1000:
    driver.find_element(By.XPATH, "//button[@class='btn btn-sm btn-primary' and text()='Gerar Certidão']").click()

    if contador == 0:
        time.sleep(6)
    else:
        time.sleep(4)

    if (len(driver.window_handles)) >= 2:
        print("Algum erro apareceu")
        exit(-1)

    print(f"Acabei de rodar pela {contador} vez")
    contador = contador + 1



