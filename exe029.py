velo = int(input("Informe a velocidade do carro em KM: "))
multa: float = (velo - 80) * 7

if velo > 80:
    print("Voce ultrapassou o limite de velocidade! Sua multa é de : R$ {:.2f} ".format(multa))
else:
    print("Você não foi multado :D")
