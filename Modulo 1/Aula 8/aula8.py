from os.path import isfile, isdir


"""
    Escrita em arquivos:
    Para essa operação utilizaremos a função open() para abrir o arquivo, 
    o método write() para escrever e o método close() para fechar o arquivo

    Métodos e funções importantes: 
    - open()
    - write()
    - close()
"""
file = open("meu_arquivo.txt","w",encoding="utf-8")
file.write("Estou assistindo a aula na turma 921")
file.close()

"""
    Modos de descrição: 
    - w: Escrita de arquivos, sobrescrevendo os dados do arquivo original (se houver)
    - a: Escrita de arquivos, adiciomando os dados ao final do arqiuvo original
    - r: Leitura de arquivo, e o modo padrão se esse parametro for omitido.
    - r+: Tanto leitura quanto escrita de arquivos (sobrescrevendo, sendo r+w)

"""

file = open("meu_arquivo","a",encoding="utf-8")
file.write("Uma frase para ser escrita no modo append\n")
file.write("Minha cor favorita é roxo\n")
file.close()

file = open("meu_arquivo","a",encoding="utf-8")
file.write("\n")
file.write("Adicionando em uma nova linha")
file.close()

file = open("meu_arquivo.txt","w",encoding="utf-8")
file.write("Algum outro texto\n")
file.write("Algum outro texto em outra linha\n")

texto = """

    Estou escrevendo um grande texto, 
    o texto fica exatamente igual com 
    aspas triplas.

"""
file.write(texto)
file.close()

file = open("meu_arquivo", "r+", encoding="utf-8") 
file.close()
"""
    Método recomendado para abertura de arquivos: with
"""

with open("meu_arquivo.txt","w",encoding="utf-8") as f: 
    f.write("Estou escrevendo com o with")


"""
    Checagem de existência de arquivos
"""

# if isfile("meu_arquivo.txt"): 
#     print("Arquivo existe")
# else: 
#     print("Arquivo nao existe")

# if isdir("arq"): 
#     print("O diretório existe")
# else: 
#     print("O diretório não existe")

# if isfile("arquivos/alessa.txt"): 
#     print("O arquivo existe")
# else: 
#     print("O arquivo não existe")

# print("Não" if isfile("meu_arquivo.txt") else "Não")



"""
    Leitura de arquivos

"""

with open('outro_arquivo.txt',"r") as file: 
    conteudo = file.read()
print(conteudo)


#limitar a quantidade de bytes lidos por vez. 1 byte = 1 caracter
#lendo 6 caracteres por vez
with open("outro_arquivo.txt", "r") as file: 
    while cinco_bytes:= file.read(5):
        print("Cinco bytes lidos:", cinco_bytes)


linhas = []
with open("outro_arquivo.txt", "r") as file: 
    for linha in file:
        linhas.append(linha.rstrip()) #rstrip elimina os \n 
        print(linha)

print(linhas)

notas = [ float(x) for x in linhas]
print(notas)