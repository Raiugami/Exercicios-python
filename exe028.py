import random
import time
print('-=-' *20)
numero = int(input("Entre 0 a 5, qual numero você acha que o computador escolheu? "))
print('-=-' *20)
n = random.randrange(0, 5)
print("processando...")
time.sleep(2)

if numero == n:
    print("Você acertou! O numero escolhido foi {}".format(n))

else:
    print("Você errou, o numero escolhido foi {}".format(n))
