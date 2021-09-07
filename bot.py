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
    erros = 0
    quant = 0

    for i, mensagem in enumerate(contatos_df['Mensagem']):

        pessoa = (contatos_df.loc[i, "NOME"]).title()
        numero = contatos_df.loc[i, "TELEFONES"]
        texto = urllib.parse.quote(f'Olá _*{pessoa}*_!\n\n{mensagem}')
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
        navegador.get(link)
        time.sleep(20)

        if len(navegador.find_elements_by_xpath(
                '//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[2]/div/div/div')) > 0:
            botao = navegador.find_element_by_xpath(
                '//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[2]/div/div/div')
            botao.click()
            erros = erros + 1

            
        elif len(navegador.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button')) > 0:
            botzinho = navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button')
            botzinho.click()
            quant = quant + 1

        while len(navegador.find_elements_by_id("side")) < 1:
            time.sleep(1)
        time.sleep(20)

    time.sleep(10)

    print(f"Lista{lista} terminada :D")
    print(f'Total de mensagens enviadas: {quant}')
    print(f'Total de numeros invalidos: {erros} ')

    continuar = str(input("Deseja continuar? [S/N] ")).upper()

    

    if continuar == "N":
        break
