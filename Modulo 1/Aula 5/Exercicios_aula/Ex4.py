"""
Desafio: função que recebe um inteiro n e printa as n primeiras linhas do triangulo e pascal. Dica funçao zip.

"""

def triangulo_pascal(num): 
    for i in range(num+1): 
        for j in range(num-i):
            print(" ",end="")
        constante = 1
        for j in range(1, i+1):
            print(constante,' ', sep='',end='')
            constante = constante * (i - j ) // j
        print()

numero_linhas = 5
triangulo_pascal(numero_linhas)