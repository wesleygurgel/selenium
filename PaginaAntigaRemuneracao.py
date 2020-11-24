from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


class PaginaAntiga:

    def __init__(self, url):
        self.url = url
        self.bot = webdriver.Firefox(executable_path='C:/Users/wesleygurgel/Downloads/geckodriver.exe')
        self.mes_atual = 0

    def abrir_navegador(self):
        driver = self.bot
        driver.get(self.url)
        driver.maximize_window()

    def escrever_campos(self, nome, cpf):
        driver = self.bot

        # Write Fields
        driver.find_element(By.ID, "Nome").send_keys(nome)
        driver.find_element(By.ID, "documento").send_keys(cpf)

    def select_ano(self, ano):
        driver = self.bot
        # Pegando o Select do Ano
        select_ano = Select(driver.find_element(By.ID, "select_ano"))
        select_ano.select_by_value(ano)

        print(len(select_ano.options))

    def select_mes(self):
        driver = self.bot

        # Pegando o Select do mês
        select_mes = Select(driver.find_element(By.ID, "select-meses-wrapper"))

        try:
            print(f'Nesse momentou estou verificando o mês {self.mes_atual}')
            select_mes.select_by_value(str(self.mes_atual))
            time.sleep(2)
            self.mes_atual += 1
            self.salvar_arquivo()

        except NoSuchElementException:
            print(f'O mês {self.mes_atual} não existe!')
            self.mes_atual += 1
            time.sleep(2)

    def salvar_arquivo(self):
        driver = self.bot
        driver.find_element(By.NAME, "Enviar").click()

    def quantidade_elementos_select(self, id):
        driver = self.bot
        # Pegando o Select do Ano
        select = Select(driver.find_element(By.ID, id))
        return len(select.options) - 1
