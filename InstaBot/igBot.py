from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\Luisb\\Documents\\Projetos\\InstaBot\\ferramentas\\geckodriver.exe") #Colocar duas contra barras para evitar erro.

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")

        time.sleep(3)

        campo_user = driver.find_element(by=By.XPATH, value='//input[@name="username"]')
        campo_user.click()
        campo_user.clear()
        campo_user.send_keys(self.username)

        time.sleep(2)

        campo_senha = driver.find_element(by=By.XPATH, value='//input[@name="password"]')
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)

        time.sleep(2)
        
        campo_senha.send_keys(Keys.ENTER)
    
    def seguir(self):
        time.sleep(4)

        driver = self.driver
        link_para_seguir = input('Insira o link da página com as pessoas a segui, na tela: ')
        time.sleep(1)
        driver.get(f"{link_para_seguir}")

        time.sleep(4)
        
        buttons = driver.find_elements(by=By.XPATH, value="//button[contains(.,'Seguir')]") #pega todos botões com o texto 'Seguir'

        try:
            for btn in buttons:
                btn.click()
                time.sleep(random.randint(5, 25))
        except:
            pass

    def comentar_sorteio(self):
        driver = self.driver
        link = input('Insira o link da publicação: ')
        time.sleep(2)
        driver.get(f'{link}')
        time.sleep(6)
        commentArea = driver.find_element(by=By.CLASS_NAME, value='_aidk')
        commentArea.click()
        commentArea.clear()
        time.sleep(2)
        frase = 'teste'
        for letra in frase:
            commentArea.send_keys(letra)
            time.sleep(random.randint(1,4)/20)
        commentArea.send_keys(Keys.ENTER)

bot = InstagramBot('user','senha')
bot.login()
bot.seguir()
bot.comentar_sorteio()