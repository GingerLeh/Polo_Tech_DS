"""
    Função que recebe como argumento uma lista e retorna uma lista com os valores unicos da lista original
"""

def lista_valor_unico(lista):
    lista_aux = []
    for i in lista: 
        if not i in lista_aux: 
            lista_aux.append(i)
    return lista_aux
        

lista = [1,1,2,2,3,3,4,4,5,5]
print(lista_valor_unico(lista))