numero = int(input("Informe um valor : "))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print("A Unidade é: {} " .format(u))
print("A dezena é: {} " .format(d))
print("A centena é: {} " .format(c))
print("A milhar é: {} " .format(m))


