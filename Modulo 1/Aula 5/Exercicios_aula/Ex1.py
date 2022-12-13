"""
    Função para calcular o máximo de três números(criando uma função auxiliar que calcular o máximo de dois números).
    Recebe 3 números e retorna o maior. 
"""

def maximo_de_dois(num1,num2): 
    if num1>num2: 
        return num1
    else:
        return num2

def maximo_de_tres(num1,num2,num3): 
    maior1 = maximo_de_dois(num1,num2)
    maior2 = maximo_de_dois(maior1,num3)
    return maior2

print(maximo_de_tres(7,4,1))