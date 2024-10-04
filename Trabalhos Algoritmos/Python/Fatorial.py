#Pede um número (n)
n = int(input())
#Iniciar o acumulador com 2 ou 1 (acum)
acum = 1
#repete de n até 2 com passo + 1 (i)
for i in range(1, (n + 1)):
    #acum = i * acum
    acum = (acum * i)
    print(i)
print (acum)