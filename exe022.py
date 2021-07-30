nome = str (input("digite seu nome completo: "))

print ("MAISCULO : ", nome.upper())
print ("minusculo : ", nome.lower())
div2 = (nome.replace(" ", ""))
print ("Contagem sem espaço: ", len (div2))
div = (nome.split())
print ("Contagem do primeiro nome ({}) : {} ".format (div[0],len (div [0])))