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


# resolução do professor. 

def pascal(row, column): 
    if row == 0 and column == 0:
        return 1
    elif row < 0 or column < 0: 
        return 0
    else: 
        return pascal(row -1, column) + pascal(row-1, column-1)


def print_pascal(n): 

    for i in range(n):
        print(" "*(n-i),end="") 
        for j in range(i + 1): 
            print(pascal(i,j),end=" ")
        print()


print_pascal(5)
