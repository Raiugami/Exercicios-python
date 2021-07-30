salario = float(input("Informe o seu salario: R$ "))
aumento = 0

if salario > 1250.00:
    aumento = salario + (salario * 0.10)
    print("O Salario ajustado é igual a: R$ {:.2f}".format(aumento))
else:
    aumento = salario + (salario * 0.15)
    print ("O Salario ajustado é igual a: R$ {:.2f}".format(aumento))
