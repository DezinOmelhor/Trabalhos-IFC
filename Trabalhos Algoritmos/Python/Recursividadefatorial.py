#Função Fatorial (n)
def fatorial(n):
    #Se n for igual a 1
    if n == 1:
    #Retorna 1
        return 1
    #Senão
    else:
        #Retorna n * fatorial (n-1)
        return n * fatorial(n - 1)
    #pede n
n = int(input("Digite um Número"))
    #x = fatorial (n)
x = fatorial(n)
#mostrar x
print (x)

#5! = 5.4! = 5.(5-1)!
#n! = n.(n-1)!
#(n-1)! = (n-1).(n-2)!
#3! = 3.2!
#2! = 2.1!
#1! = 1