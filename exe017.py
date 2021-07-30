import math

oposto = float (input("Informe o cateto oposto: "))
ad = float  (input("informe o cateto adjacente: "))
hipotenusa = math.hypot(oposto,ad)
print ("A hipotenusa equivale a: {:.2f}".format(hipotenusa))