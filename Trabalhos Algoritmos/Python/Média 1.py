#Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno.
a = float(input())
b = float(input())
x = a * 3.5 + b * 7.5
#calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11)
y = x / 11
#Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
#Imprima a mensagem "MEDIA" e a média do aluno, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade.
print(f"MEDIA = {y:.5f}")
#Utilize variáveis de dupla precisão (double) e como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".' 