from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


class PaginaNova:

    def __init__(self, url):
        self.url = url
        self.bot = webdriver.Firefox(executable_path='geckodriver.exe')

    def abrir_navegador(self, login="wesleygurgel", senha="Bilubilu123@"):
        driver = self.bot
        driver.get(self.url)
        driver.maximize_window()
        time.sleep(1)

        driver.find_element_by_xpath('//a[@href="/transparencia/protegido"]').click()
        driver.find_element(By.ID, "username").send_keys(login)
        driver.find_element(By.ID, "password").send_keys(senha)
        time.sleep(1)

        driver.find_element(By.NAME, "login").click()
        time.sleep(2)

        driver.get(self.url)
        time.sleep(1)

    def escrever_campos(self, ano, mes, cpf="70383775400", formato=".pdf"):
        try:
            driver = self.bot

            if ano == "2019" or ano == "2020":
                formato = ".xls"

        # ABRIR O FORM
            driver.find_element(By.XPATH, "//button[@class='btn btn-success' and text()=' Item']").click()
            time.sleep(1)

        # A PARTIR DAQUI JÁ ESTAMOS NO FORM
            driver.find_element(By.XPATH, "//div/form/div/input").send_keys('transparencia-' + ano + '-' + mes)

            select_ano = Select(driver.find_element(By.XPATH, "//div/form/div/select[@id='ano']"))
            select_ano.select_by_value(ano)
            select_mes = Select(driver.find_element(By.XPATH, "//div/form/div/select[@id='mes']"))
            select_mes.select_by_value(mes)

        # Escrevendo no TEXTAREA - DESCRIÇÃO
            driver.find_element(By.XPATH, "//div/form/div/textarea").send_keys('transparencia-' + ano + '-' + mes)

        # UPLOAD ARQUIVOS
            driver.find_element(By.ID, "arquivo0").send_keys(
                "C:\\Users\\wesleygurgel\\Downloads\\transparencia-" + ano + "-" + mes + formato)
            driver.find_element(By.NAME, "formCadastro").click()
            driver.find_element(By.XPATH, "//div/form/div/button[@type='submit']").click()
            time.sleep(1)

        except NoSuchElementException:
            print(f'O mês {mes} ou {ano} não existe no Forms!')
            driver.find_element(By.XPATH, "//div/form/div/button[@type='button']").click()
            time.sleep(2)

        except InvalidArgumentException:
            print(f'Não tem arquivo esse {mes}')
            driver.find_element(By.XPATH, "//div/form/div/button[@type='button']").click()
            time.sleep(2)
