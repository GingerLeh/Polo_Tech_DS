"""
Faça uma função chamada ordena_palavras que recebe uma string de palavras seperadas por vírgulas, 
por exemplo "vermelho,roxo,azul,vermelho", e retorne as palavras únicas ordenadas em ordem lexicográfica.

ordena_palavras("vermelho,roxo,azul,vermelho") -> "azul,roxo,vermelho"
"""


def ordena_palavras(texto): 
    texto = texto.lower()
    lista_aux =[]
    palavras = texto.split(",")
    for p in palavras: 
        if p not in lista_aux: 
            lista_aux.append(p)
    palavras = lista_aux.copy()
    lista_aux = []
    for i in range(len(palavras)): 
        if i == 0:
            menor_palavra = palavras[i]
            lista_aux.insert(0, menor_palavra)
        if palavras[i] < menor_palavra: 
            menor_palavra = palavras[i]
            lista_aux.insert(0, menor_palavra)

    return print(",".join(lista_aux))

ordena_palavras("vermelho,roxo,azul,vermelho")

