import pandas as pd
from selenium import webdriver
import time
import urllib

from selenium.webdriver.common.keys import keys

contatos_df = pd.read_excel ("lista1.xlsx")
display(contatos_df)

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id ("side")) < 1:
    time.sleep(1)
# Já estamos com o login feito no whatsapp web

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i,"NOMES"]
    numero = contatos_df.loc[i,"TELEFONES"]
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"