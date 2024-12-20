# Fazer o cálculo do tamanho máximo do Pen drive (1 GB)
TAMANHO_MAX = 1 * 1024 * 1024 * 1024

# Vetor com os tamanhos dos arquivos (em bytes)
a = [300 * 1024 * 1024, 500 * 1024 * 1024, 700 * 1024 * 1024, 400 * 1024 * 1024]

# Ordena os tamanhos em ordem decrescente
a.sort(reverse=True)

# Inicializa as variáveis
usos = 0
while a:
    capacidade_restante = TAMANHO_MAX
    i = 0
    # Remove arquivos que cabem na capacidade restante
    while i < len(a):
        if a[i] <= capacidade_restante:
            capacidade_restante -= a[i]
            a.pop(i)
        else:
            i += 1
    usos += 1

# Exibe o número de usos necessários
print(f"Será necessário usar o pen drive {usos} vez(es).")