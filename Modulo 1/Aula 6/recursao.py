"""
    Recursão: 
    Esse é um dos coiceitos mais importantes de funções em ciência da computação.
    É um método de resolução de problemas que envolve quebrar um problema em subproblemas
    menores e menores até chegar a um problema pequeno o suficiente para que se posa ser resolvido trivialmente. 

    As três leis da recursão: 
    1. Um algoritmo recursivo deve ter um caso básico; 
    2. Um algoritmo recursivo deve mudar seu estudo e se aproximar no caso básico; 
    3. Um algotitmo recursivo deve chamar a si mesmo, recursivamente. 
"""

# Exemplo de fatorial: 
def fatorial (n):
    if n == 0: 
        return 1
    if n == 0: 
        return 1
    return n * fatorial(n-1)


print(fatorial(4))

def fib(n):
    if n ==1: 
        return 1
    if n == 2: 
        return 1
    return fib(n-1) + fib(n-2)

print(fib(4))

# While recursivo

def while_recursivo(n): 
    if n == 1: 
        print(n)
    else:
        print(n)
        while_recursivo(n-1)

print(while_recursivo(5))

# Calculando a soma de uma lista de numeros 

def soma_recursao(lista): 
    if len(lista) ==1: 
        return lista[0]
    return lista[0] + soma_recursao(lista[1:])
lista = [3,6,7,8]
print(soma_recursao(lista))