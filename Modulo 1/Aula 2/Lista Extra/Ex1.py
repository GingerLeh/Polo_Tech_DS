"""
Faça um programa que recebe a idade de 3 pessoas e imprima quem é a pessoa mais velha e quem é a mais nova.

Não usar funções min, max etc.
"""

idade_pessoa1 = int(input("Digite a idade da primeira pessoa: "))
idade_pessoa2 = int(input("Digite a idade da segunda pessoa: "))
idade_pessoa3 = int(input("Digite a idade da terceira pessoa: "))

if(idade_pessoa1 > idade_pessoa2 and idade_pessoa1 > idade_pessoa3): 
    print(f"Primeira pessoa é a mais velha das três com {idade_pessoa1} anos")
elif(idade_pessoa2>idade_pessoa1 and idade_pessoa2 > idade_pessoa3):
    print(f"Segunda pessoa é a mais velha das três com {idade_pessoa2} anos")
else:
    print(f"Terceira pessoa é a mais velha das três com {idade_pessoa3} anos")

