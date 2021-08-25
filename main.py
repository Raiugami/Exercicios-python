import pandas as pd
from selenium import webdriver
import time
import urllib
import os

continuar = "S"

print('''                                                                                                                         
                                                                                                              
  ||||      ||||      |||| ||||                                                                                         
  ||||     ||||||     |||  ||||                        ||||                                                             
   |||     ||||||    ||||  ||||                        ||||               |||||||||||      ||||||||||    |||||||||||||  
   ||||    ||||||    |||   |||| ||||||    |||||||||   ||||||||   |||||||||||      ||||   |||       ||||      |||        
    |||   ||| ||||   |||   |||||| |||||   |     ||||   ||||     |||    ||||       |||   |||         |||      |||        
    ||||  |||  |||  |||    |||||    |||          |||   ||||     |||||    ||       |     ||          ||||     ||         
     |||  ||   |||| |||    ||||     |||   ||||||||||   ||||      ||||||||||||||||||    |||          ||||    |||         
     |||||||    ||||||     ||||     |||  ||||    |||   ||||          ||||||      |||   |||          |||     |||         
      |||||     ||||||     ||||     |||  ||||   ||||   |||||||  ||    |||||       |||  |||          |||     |||         
       ||||      ||||      ||||     |||   ||||||||||    ||||||  |||||||||||      ||||   |||        |||     |||          
       ||||      ||||      ||||     |||    ||||  |||     ||||     |||||||||||||||||      |||||||||||       |||          
                                                                       |||||||||||        ||||||||         |||               \n''')

while continuar != "N":
    lista = str(input("Informe o numero da lista: "))

    contatos_df = pd.read_excel(f"lista{lista}.xlsx")

    navegador = webdriver.Chrome()
    navegador.get("https://web.whatsapp.com/")

    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)

    # Já estamos com o login feito no whatsapp web

    def dados():
        pessoa = (contatos_df.loc[i, "NOME"]).title()
        numero = contatos_df.loc[i, "TELEFONES"]
        texto = urllib.parse.quote(f'Olá _*{pessoa}*_!\n\n{mensagem}')
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
        navegador.get(link)
        time.sleep(15)

    def esperar():
        while len(navegador.find_elements_by_id("side")) < 1:
            time.sleep(1)
        time.sleep(7)

    def condicao():
        if len(navegador.find_elements_by_xpath(
                '//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[2]/div/div/div')) > 0:
            botao = navegador.find_element_by_xpath(
                '//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[2]/div/div/div')
            botao.click()
        elif len(navegador.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button')) > 0:
            botzinho = navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button')
            botzinho.click()


    for i, mensagem in enumerate(contatos_df['Mensagem']):

        dados()

        condicao()

        esperar()

        time.sleep(10)



    continuar = str(input("Deseja continuar? [S/N] ")).upper()

    os.system('cls') or None

    if continuar == "N":
        break
