"""
Faça um programa que recebe um número e imprime o valor absoluto do número. Ex:

INPUT = 1 OUTPUT = 1 INPUT = -1 OUTPUT = 1

Não usar a função abs().
"""

numero = int(input("Digite um numero: "))

if(numero < 0): 
    numero = numero * -1
    print(f"Número absoluto: {numero}")
else: 
    print(f"Número absoluto: {numero}")
