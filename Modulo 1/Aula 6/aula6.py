"""
    Lidando com strings: 

    Aplicações importantes: 
    - Converter texto recebido do usuário para um formato entendível pelo computador.
    - Recuperar dados guardados em um sistema
    - Processar dados formatados
    ...
"""


"""
    Extraindo parte de strings

    A parte extraída de uma string é chamada substring. Para extrair uma substring usamos a seguinte sintaxe: 
        palavra[inicio:fim]

    Isso retorna um texto começando a partir do caracter de indice inicio e termino de indice fim -1. 

    Por exemplo, a seguinte string tem os seguintes índices: 
    0123456789
    Let's Code

    Se quisermos extrair "Code", podemos fazer o seguinte: 
"""

minha_string = "Let's Code"
print(minha_string[6:10])
#outra forma seria [6:-1]
print(minha_string[::-1])

print(minha_string[:5])
print(minha_string[-4:])
print(minha_string[::2])

"""
    Iterando strings: 
    
    A iteração de strings acontece de forma similar a uma lista

""" 
for caracter in minha_string:
    print(caracter)

for indice, caracter in enumerate(minha_string): 
    print(f"Índice: {indice} Caracter: {caracter}")

"""
    Métodos de strings: 

    - upper() ->  Transforma todas as letras em maiúsculas
    - lower() ->  Transforma todas as letras em minúsculas
    - title() -> Transforma a primeira letra de cada palavra em minúscula
    - replace() -> Substitui uma expressão por outra
    - split() -> Divide a string a partir de um caractere separador
    - join() -> Utiliza a string para juntar os elementos de uma lista
"""
string_modificada = "Let's Code".replace("e","a")
print(f"Método upper():{minha_string.upper()}")
print(f"Método lower():{minha_string.lower()}")
print(f"Método title():{minha_string.title()}")
print(f"Método replace():{string_modificada}")
print(f"Método split():{minha_string.split(' ')}")

string_csv = 'Altura, Idade, Nome, Profissão'
print(string_csv.split(","))

string_arquivo = "1800\n1500\n800"
print(string_arquivo.split("\n"))


lista = ["Essa","é","minha","string"]
string_vazia = ""
for palavra in lista: 
    string_vazia += palavra
    string_vazia += " "
print(string_vazia)

print(" ".join(lista))
print("\n".join(lista))
print("*".join(lista))

"""
    Caracteres ASCII
    - Para acessar o valor de um caracter ASCII: ord(c)
    - Dado um inteiro para acessar o caracter associado: chr(n)
"""
print(ord("A"))
print(chr(65))

inicio_maiusculo = ord("A")
inicio_minusculo = ord("a")
diference = inicio_minusculo - inicio_maiusculo
b_maiusculo = ord("B")
b_minusculo = b_maiusculo + diference
print(b_minusculo)
print(chr(b_minusculo))

shifted_letter = ord("A") +4
print(chr(shifted_letter))