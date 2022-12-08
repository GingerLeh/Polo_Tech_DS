"""
Faça um programa que recebe dois valores inteiros do usuário e indique o maior entre os dois.

Além disso, faça uma validação dos dados recebidos. Por exemplo, se o programa receber um float 
ou string deve retornar que os valores recebidos são inválidos.

"""

valor1 = int(input('Digite o primeiro numero: '))
valor2 = int(input('Digite o segundo numero: '))

if(valor1>valor2):
    print(f"{valor1} é maior que {valor2}")
else:
    print(f"{valor2} é maior que {valor1}")
