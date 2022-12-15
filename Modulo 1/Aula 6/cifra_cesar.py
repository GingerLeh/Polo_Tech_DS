
def criptografa(palavra,chave): 
    palavra = palavra.lower()
    lista_da_palavra = []
    for p in palavra: 
        if p == "z" or p == "y" or p == "w" or p == "x":
            ponteiro = ord("a")
            nova_letra = ponteiro + (chave-1)
            lista_da_palavra.append(chr(nova_letra))
        else:
            ponteiro = ord(p)
            nova_letra = ponteiro + chave
            lista_da_palavra.append(chr(nova_letra))
    return print("".join(lista_da_palavra))

def descriptografa(palavra,chave):
    palavra = palavra.lower()
    lista_da_palavra = []
    for p in palavra: 
        if p == "a" or p == "b" or p == "c" or p == "d":
            ponteiro = ord("z")
            nova_letra = ponteiro
            lista_da_palavra.append(chr(nova_letra))
        else:
            ponteiro = ord(p)
            nova_letra = ponteiro - (chave)
            lista_da_palavra.append(chr(nova_letra))
    return print("".join(lista_da_palavra))

criptografa("alessa",4)
descriptografa("epiwwe",4)


#do professor: 

def codifica_cesar(texto, desclocamento): 
    begin = ord("a") - ord("a")
    end = ord ("z") - ord("a")
    codificado = ""
    for c in texto: 
        if c != " ": 
            index_c = ord(c) - ord("a")
            new_index_c = index_c +desclocamento
            if new_index_c >end: 
                new_index_c = new_index_c%(end-begin+1)
            codificado += chr(new_index_c + ord("a"))
        else: 
            codificado +=c
        return codificado

cod = codifica_cesar("oi meu nome é lucas", 4)
cod = codifica_cesar("", -4)




