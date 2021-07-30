import math
angulo = float (input("informe um ângulo qualquer: "))
seno = math.sin (math.radians(angulo))
cosseno = math.cos (math.radians(angulo))
tangente = math.tan (math.radians(angulo))
print("O valor de seno é {:.2f} , cosseno {:.2f} e tangente {:.2f}" .format (seno,cosseno,tangente))
