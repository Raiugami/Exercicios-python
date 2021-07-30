import random

a1 = input("Informe o nome do primeiro aluno: ")
a2 = input("Informe o nome do segundo aluno: ")
a3 = input("Informe o nome do terceiro aluno: ")
a4 = input("Informe o nome do quarto aluno: ")

print ("O Aluno escolhido foi: {}" .format(random.choice([a1, a2, a3, a4])))