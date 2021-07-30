a = float(input("informe o lado A do triangulo: "))
b = float(input("informe o lado B do triangulo: "))
c = float(input("informe o lado C do triangulo: "))

if b-c < a < b + c and a-c < b < a+c and a-b < c < a+b:
    print("Pode formar um triangulo!")
else:
    print("Não pode formar um triangulo!")
