# Declara as variáveis para contar
a = (0)
b = (0)
c = (0)
d = (0)
# Para até 20 valores serem dados ou um número abaixo de zero
for _ in range(20):
    n = int(input("Digite um número "))     # Declara 'n' como a variável dada pelo usuário
    if n < 0:                       # Se o número for menor que 0
        break                       # Encerra o programa
    if 0 <= n <= 25:                # Se o número for maior ou igual a 0 e menor ou igual a 25
        a = (a + 1)                 # Soma 1 em 'a'
    elif 26 <= n <= 50:             # '' '' ''
        b = (b + 1)                 # ''
    elif 51 <= n <= 75:             # ''
        c = (c + 1)                 # ''
    elif 76 <= n <= 100:            # ''
        d = (d + 1)                 # ''
# Mostra os resultados (a,b,c,d)
print ("A quantidade de números entre [0 - 25] é de", a)
print ("A quantidade de números entre [26 - 50] é de", b)
print ("A quantidade de números entre [51 - 75] é de", c)
print ("A quantidade de números entre [76 - 100] é de", d)