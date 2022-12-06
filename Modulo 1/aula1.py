# Referências utilizadas sobre python e vcscode
# https://www.python.org
# https://python.org.br
# Documentação oficial: https://docs.python.org/pt-br/3/tutorial/
# Playlist python: https://www.youtube.com/watch?v=cDqMbI02hRs&list=PLcmVV8telDGzH6wFY_9h_KZ3Sn7EfjT1D
# https://www.blog.duomly.com/tags/python/
# Representação de ponto flutuante: https://learn.microsoft.com/pt-br/cpp/build/ieee-floating-point-representation?view=msvc-170




## 1 - Sintaxe em python 


## Vamos começar imprimindo "Hello World!" na sáida padrão
## Para imprimir utilizamos a função print(), perceba que para utilizar funções 
## usamos os parenteses(). E dentro dos parenteses passamos o que a função precisa ser executada. 

## O caso de uso mais simples do print é o seguinte: 

print ("Hello World!")

## Também podemos rodar a função print usando o argumento com aspas simples '
print ('Hello World')

## Posso chamar a função print sem nenhum argumento. Isso imprime uma linha vazia.
print()

## Note que não precisamos de ; entre cada comando. 

####### 1.1 Comentários

'''
isso comenta um bloco de comentario
posso continuar comentando na linha de baixo 
por exemplo
'''

'''
Configurar atalho para rodar o python: configurações > teclas de atalho >> *busca o pyrthon:run python*
'''

## Podemos usar essa funcionalidade para omitir parte do código 

'''
print ("oi")
a = 3
b = 7
x = a + b
'''

####### 1.2 Variáveis

"""
    As variáveis são elementos que armazeram alguma informação na memória do computador, i.e, a RAM.
    Podemos guardar variáveis: números, textos, dados de entrada, estrutura de dados complexas (grafos, árvores binárias, etc)
    A variável representa duas coisas: o endereço de memórias para qual ela aponta o conteúdo do endereço
"""

nome = "Lets Code"

"Mais uma forma de usar o print"
print("Hello " + nome) # entretanto o nome sai colado junto com hello -> para resolver podemos dar um espaço depois do Hello
print("Hello " + nome +"!")

####### 1.3 Tipagem de dados 

"""
    Tipagem é o tipo da informação que armazenamos. 
    Acima atribuímos um texto à variável nome. 
    Muitas linguagens são chamadas "linguagens estáticas" porque exigem que o tipo da variável seja especificada. Por exemplo,
    em c fazemos int x. 

    No python, não precisamos definir o tipo da variável. O python é uma linguagem dinâmica. 
"""

nome = "1" # uma string
print("Hello" + nome)

nome = 1 # como não colocamos aspas isso se torna um numero (int nesse caso)
# print ("Hello" + nome + "!") # Obtemos o seguinte erro com o comando acima: TypeError: can only concatenate str (not "int") to str

"""
    Isso diz que não podemos concatenar um int com str, somente str com str. 

    str: é um texto. Exemplo: qualquer texto representado entre '' ou "", como "Lets Code". 

    int: faz referencia a números inteiros, sendo uma abreviação de integer. Exemplo: -150, 0, 12345678567
        Detalhe: o maior número inteiro que podemos representar depende da arquitetura do processador (32 bits ou 64 bits)

    float: representa números reais, recebendo o nome floating point por causa da forma que esses números são armazenados no computador
        Exemplo: -1234324.4, 0.0000000001, 10E-3, 15.0

    bool: representa valores True e False, valores de Álgebra Booleana. Usamos para indicar a existência ou validade de algum parâmetro.

    Esses são os principais tipos da linguagem python -> tipos primitivos. 

    Python é uma linguagem fortemente tipada, pois não altera o tipo do dados para realizar algum tipo de opração. 

    No caso de uma linguagem fracamente tipada, a linguagem faz uma coerção do tipo da variável para que a operação seja realizada. 
        Ex: A linguagem tenta converter 1 (int) para "1" (str) de forma a concatenação ocorra. Vamos nos referir a isso como casting.
"""

## Podemos verificar facilmente o tipo das variáveis usando a função type()

print(type("texto"))
print(type(1))
print(type(1.0))
print(type(True))

# Referências sobre tipagem: 
#       https://www.sitepoint.com/why-is-a-string-called-a-string/
#       https://pt.wikipedia.org/wiki/Álgebra_booliana