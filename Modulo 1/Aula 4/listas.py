### Sintaxe
minha_lista = [5, True, "Lucas", ["elemento dentro da lista",[3, False]]]
print(minha_lista)

### Listas têm tamanho dinâmico. Ou seja, tem tamanho variável.


### Índices

print(f"O primeiro elemento da minha lista é {minha_lista[0]}")
print("O segundo elemento da minha lista é:", minha_lista[1])
print("O terceiro elemento da minha lista é:", minha_lista[2])
print("O quarto elemento da minha lista é:", minha_lista[3])

### Como o quarto elemeneto é uma lista:

print("O primeiro elemento da lista-4 é:", minha_lista[3][0])
print("O segundo elemento da lista-4 é:", minha_lista[3][1])

### Iterando em listas

for elemento in minha_lista:
    if (type(elemento) == str):
        continue
    print("Elemento:", elemento)
### função enumerate

for indice, elemento in enumerate(minha_lista):
    print(f"Índice: {indice}  Elemento: {elemento}")

for i in range(0, len(minha_lista)):
    print(f"Índice: {i}    Elemento: {minha_lista[i]}")


a, _ = (5, 6)
print(a)


### Funções Últeis

minha_lista = [1, 5, -1, 19]
valor_max = max(minha_lista)
print(f"Valor máximo da lista é: {valor_max}")


minha_lista = ["Lucas", "Ana", "Ze"]
valor_max = max(minha_lista, key = lambda x : len(x))

"""
    lambda x: x[1] vai aplicar x[1] para cada elemento da minha_lista
    Então, procurará o maior entre [u, n, e]
    O elemento máximo dessa lista é u, que corresponde a Lucas

"""


print(f"Valor máximo da lista é: {valor_max}")

minha_lista = [[1, 5, 6], [6, 3, 1], [2, 3, 4]]
valor_max = max(minha_lista, key = sum)  #<---- Sum retorna a soma dos valores da lista
"""
    lambda x: sum(x) vai aplicar soma a cada lista, obtende a seguinte lista: [12, 10, 9]
    O maior elemento é o 12, que corresponde a [1, 5, 6]
"""


print(f"Valor máximo da lista é: {valor_max}")

#minha_lista = [[1, 5, 6], [6, "Lucas", 1], [2, 3, 4]]
#valor_max = max(minha_lista, key = lambda x : x[1])  #<---- Sum retorna a soma dos valores da lista
#print(f"Valor máximo da lista é: {valor_max}")


print(f"A lista {minha_lista} tem tamanho {len(minha_lista)}")

minha_lista = []
print(f"A lista {minha_lista} tem tamanho {len(minha_lista)}")

meu_flotat = 123490
meu_float_string = str(meu_flotat)
print(f"O tamanho da string {meu_float_string} é {len(meu_float_string)}")


#### append() : maneira de adicionar elementos no final da lista

minha_lista = []

#queremos adicionar a letra "a" a lista

minha_lista.append("a")
print(minha_lista)

minha_lista.append("b")
print(minha_lista)


### insert(): adicina em determinado indice

minha_lista.insert(1, "c")
print(minha_lista)

minha_lista.insert(0, "d")
print(minha_lista)

minha_lista.insert(1, "c")
print(minha_lista)

minha_lista.remove("c") #<--- remove o primeiro elemento encontrado
print(minha_lista)

removido = minha_lista.pop()      # <--- remove o ultimo elemento da lista 
print(f"Elemento removido {removido}")
print(minha_lista)


### Slicing em listas
"""
    Slicing é uma operação de corte da lista. é a operação que usamos quando
    queremos obter apenas parte da lista

    Sintaxe:
        minha_lista[Inicio : Fim : Passo]

"""

"""
    Para retonar o elemento de indice i da lista: lista[i]
"""



lista = [50, 70, 30, 20, 90, 10, 50]
print(lista[::])


### A lista aceita indices negativos:
ultimo = lista[-1]
print(f"O último elemento da lista é {ultimo}")
print(f"O penúltimo elemento da lista é {lista[-2]}")

"""
    i = 0 1 2 3 4 5
        -6  -5  -4  -3  -2  -1
"""

print(lista[-7::])


print(lista[::-1])

###inversão de strings:

nome = "LUCAS"
print(nome[::-1])


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista[3:9:2])

print(lista[::2])


#### Copias de listas:

# copia rasa

lista = [1, 2, 3]
#lista_copia = lista.copy()
lista_copia = lista[:]   #<----copia rasa cria uma nova lista com os valores da lista original, assim as mudanças de uma não refletem na outra
#lista_copia = lista #<--- por referencia: alteração em uma lista refleta na outra
lista[0] = -10
lista_copia[1] = 5

print(f"Original: {lista} Cópia: {lista_copia}")

#copia profunda

import copy

lista = [[1, 2], [3, 4]]
#lista_copia = lista.copy() #<-- copia rasa
lista_copia = copy.deepcopy(lista) 
#lista_copia = lista[:]   #<---- copia rasa

lista[0][0] = -1

print(f"Original: {lista} Cópia: {lista_copia}")

### Compreensão de listas

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
minha_lista = []
for fruit in fruits:
    if "a" in fruit:
        minha_lista.append(fruit)

print(minha_lista)

minha_lista2 = [fruit for fruit in fruits if "a" in fruit]
print(minha_lista2)

"""
    nova_lista = [expressao for item in lista if condition == True]

"""

minha_lista = [1, 2, 3, 4, 5]
nova_lista = [x**2 for x in minha_lista]
print(nova_lista)

# Com if sem else
nova_lista = [x**2 for x in minha_lista if x%2==0]
print(nova_lista)

## com if-else
nova_lista = [x**2 if x % 2 == 0 else x**3 for x in minha_lista]
print(nova_lista)

## criar lista com valroes de 1 a n:

nova_lista = [x if x%2 != 0 else x**2 for x in range(1, 11)]
print(nova_lista)

nova_lista = [x for x in minha_lista]
minha_lista[0] = -1
print(nova_lista)










### stacks - pilha

"""
    É uma estrura de dado do tipo first-in last-out. Primeiro que entra sai por último.
               3
         2     2    2
    1 -> 1  -> 1 -> 1 -> 1 -> _

"""

#stack = []
#stack.append("a")
#print(stack)
#stack.append("b")
#print(stack)
#stack.append("c")
#print(stack)
#
#stack.pop()
#print(stack)
#
#stack.append("d")
#print(stack)
#
#
#stack.pop()







