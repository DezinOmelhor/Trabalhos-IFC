string = input("Digite uma string: ")   # Pede uma string ao usuário
inverso = ""                            # Cria uma variável para armazenar a string invertida
for i in range(len(string) -1, -1, -1):    # Passa a string de trás para frente
    inverso += string[i]
print(inverso)                               # Mostra o inverso da string
