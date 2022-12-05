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
print("Hello" + nome)# entretant o nome sai colado junto com hello
print("Hello" + nome +"!")

####### 1.3 Tipagem de dados 
