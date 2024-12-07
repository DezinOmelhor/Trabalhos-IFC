# Criar vetor para tradução de português e Inglês
port = ["como", "oi", "bonito", "azul"]
ing = ["how", "hello", "beatiful", "blue"]

f = input("Digite uma frase in english: ")      # Pedir uma frase em inglês
p = f.split()                                   # Dividir essa frase por palavras

# Traduzir as palavras
t = []                                      # Declarar tradução como lista
for palavra in p:                           # Para cada "Palavra" em palavras(p)
    if palavra in ing:                      # Se a palavra estar em ingles
        t.append(port[ing.index(palavra)])  # Tradução "puxa" o equivalente em portugues e verifica se há a tradução em ingles, para substitui-lo
    else:                                   # Senão
        t.append(palavra)                   # Mantém a palavra em inglês
# Mostrar frase depois de traduzida
print (" ".join(t)) 