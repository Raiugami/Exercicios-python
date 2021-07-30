n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
n3 = int(input("Informe o terceiro numero: "))

if n1 > n2 and n1 > n3 and n2 > n3:

    print("O maior numero é {}".format(n1))
    print("O menor numero é {}".format(n3))
elif n2 > n3 and n3 > n1:
    
    print("O maior numero é {}".format(n2))
    print("O menor numero é {}".format(n1))
else:
    print("O maior numero é {}".format(n3))
    print("O menor numero é {}".format(n2))
