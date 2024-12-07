n = int(input("Quantos números deseja informar? "))  # Número total de entradas
a = 0  # Variável para acumular a soma dos resultados
m = 1  # Fator multiplicador inicial

for _ in range(n):  # Itera 'n' vezes
    numero = int(input("Digite um número: "))  # Lê o número
    a += numero * m  # Multiplica o número pelo fator atual e soma ao total
    m += 1  # Incrementa o multiplicador

print("Soma dos cálculos:", a)  # Exibe o resultado
