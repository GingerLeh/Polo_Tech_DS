"""
A média ponderada funciona de forma parecida a média aritmética, as levando em consideração o peso de cada número 
utilizado no cálculo. O objetivo do exercício será montar um código para o cálculo da média ponderada conforme a equação abaixo:


$$ \bar{x} = \frac{w1P + w2L + w3*T}{w1 + w2 + w3}$$


Onde $P$ é a média de 3 provas, L é a nota em relção a entrega das Listas de exercicios 
(onde cada lista entregue conta como 1 ponto sendo um total de 10 listas) e T é a nota do Trabalho, onde w1, w2 e w3 
são os respectivos pesos. Você deve desenvolver um código onde irá receber as notas das 3 provas (e calcular a média), 
irá receber quantas listas o aluno entegou entre as 10 totais e receber a nota do Trabalho. Por fim para os 
pesos $w1 = 0.4$, $w2 = 0.1$ e $w3 = 0.5$, devolva o valor da média ponderada do aluno.
"""

prova1 = float(input("Digite a nota da primeira prova: "))
prova2 = float(input("Digite a nota da segunda prova: "))
prova3 = float(input("Digite a nota da terceira prova: "))
trabalho = float(input("Digite a nota do trabalho: "))
listas = int(input("Digite quantas listas o aluno entregou (máximo de 10): "))

total = prova1 + prova2 + prova3 
media = total/3 

ponderada = (0.4*media + 0.1 *listas + 0.5*trabalho)/(0.4 + 0.1 + 0.5)

print(f"A média ponderada do aluno foi: {ponderada}")
