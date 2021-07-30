dist = int(input("Informe a distancia da sua viagem em KM: "))
valor: float = 0
if dist > 200:
    valor = dist * 0.45
    print("O valor da viagem é: R$ {:.2f}".format(valor))
else:
    valor = dist * 0.50
    print("O valor da viagem é: R$ {:.2f}".format(valor))
