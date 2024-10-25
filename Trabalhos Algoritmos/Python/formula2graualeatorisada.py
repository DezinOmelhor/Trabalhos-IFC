import math
#Pedir 3 numeros ao usuario
a = float(input("Digite um numero 1/3 "))
b = float(input("Digite um numero 2/3 "))
c = float(input("Digite um numero 3/3 "))
#Calcular delta
d = ((b**2) - (4*a*c))
#Se delta for menor que 0, mostrar que não existe raiz
if (d < 0):
    print("Não há raiz",)
#Se não, se delta for igual a 0, calcular e mostrar que só há uma raiz
elif (d == 0):
    u = (-b/2*a)
    print("A raiz é",u)
#se não, se delta for maior que 0, calcular e mostrar as duas raizes
elif(d > 0):
    u = (-b + math.sqrt(d)/2*a)
    o = (- b - math.sqrt(d)/2*a)
    print("As raizes são %f e %f \n",u,o,)