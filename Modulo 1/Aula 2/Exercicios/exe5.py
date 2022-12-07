"""
O desvio padrão é uma métrica de dispersão onde avalia o espalhamento dos dados em uma determinada distribuição. 
A equação para o cálculo do desvio padrão é dada por:


σ=√ Σ n,i=1 (xi−x¯)^2/n−1

Monte um código que receba 10 valores inteiros que variem entre 1 e 10, e retorne os valores da média e desvio 
padrão destes 10 valores. Para auxiliar no desenvolvimento, siga os passos a seguir:

Receba os 10 números inteiros;
Calcular a média dos múmeros;
Calcule as diferenças em relação a média ao quadrado;
Cacule a soma das diferenças;
Calcule o desvio padrão.

"""

import math

valor1 = int(input("Digite o primeiro valor que varia de 1 a 10: "))
valor2 = int(input("Digite o segundo valor que varia de 1 a 10: "))
valor3 = int(input("Digite o terceiro valor que varia de 1 a 10: "))
valor4 = int(input("Digite o quarto valor que varia de 1 a 10: "))
valor5 = int(input("Digite o quinto valor que varia de 1 a 10: "))
valor6 = int(input("Digite o sexto valor que varia de 1 a 10: "))
valor7 = int(input("Digite o sétimo valor que varia de 1 a 10: "))
valor8 = int(input("Digite o oitavo valor que varia de 1 a 10: "))
valor9 = int(input("Digite o nono valor que varia de 1 a 10: "))
valor10 = int(input("Digite o décimo valor que varia de 1 a 10: "))

total = valor1 + valor2 + valor3 + valor4 + valor5 + valor6 + valor7 + valor8 + valor9 + valor10
media = total/10
desvio_nota1 = media - valor1
desvio_nota2 = media - valor2
desvio_nota3 = media - valor3
desvio_nota4 = media - valor4
desvio_nota5 = media - valor5
desvio_nota6 = media - valor6
desvio_nota7 = media - valor7
desvio_nota8 = media - valor8
desvio_nota9 = media - valor9
desvio_nota10 = media - valor10

variancia = (desvio_nota1**2 + desvio_nota2**2 + desvio_nota3**2 + desvio_nota4**2 + desvio_nota5**2 + desvio_nota6**2 + desvio_nota7**2 + desvio_nota8**2 + desvio_nota9**2 + desvio_nota10**2)/10
desvio_padrao = math.sqrt(variancia)

print(f"O desvio padrão é: {desvio_padrao}")


#calculo feito com base no vídeo: https://www.youtube.com/watch?v=JEwd0Vlqapo