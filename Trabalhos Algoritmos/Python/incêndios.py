#Faça um programa que leia um arquivo texto que contém dados sobre incêndios e conte quantos incêndios ocorreram em um determinado ano informado pelo usuário.
#Pedir um arquivo de texto e listar os anos
with open('/home/ifc/Área de trabalho/.Py/exemplo.txt', 'r') as arquivo:
        ano_pedido = input("Digite o ano ")
        Incendios = 0
        for linha in arquivo:
            partes = linha.strip().split(',')
            ano = partes[0].strip()
        #Contar incêndios por ano
            if ano == ano_pedido:
              Incendios += int(partes[3])
        print(Incendios)
#print o número de incendios do ano pedido pelo usuário