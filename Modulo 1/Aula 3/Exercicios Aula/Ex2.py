"""
    Conjectura de collatz: 

    Dado um número n>=1. 
    Se n for impar, atualize n -> 3n+1
    Se n for par, atualize n -> n/2
    Faça até n virar 1

    6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

    Faça um programa que escreva a sequencia dos valores até chegar em 1. 
"""

numero = int(input("Digite o número:")) 

while True: 
    
    if numero%2==0: 
        numero =  numero/2
    else: 
        numero = numero*3+1
    
    if numero == 1:
        print(f"{int(numero)}"," ", end = "")
        break
    print(f"{int(numero)}"," ", end = "", sep=" ->")