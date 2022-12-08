# Artigo do professor: https://medium.com/turing-talks/como-machine-learning-consegue-diferenciar-heterônimos-de-fernando-pessoa-156d0d52a478
# Outro artigo: https://pages.cs.wisc.edu/~gfung/federalist.pdf
# Turing completude: https://pt.wikipedia.org/wiki/Turing_completude

"""
    Estruturas condicionais - Introdução 

    As estruturas condicionais são parte fundamental de uma linguagem de programação. 

    São estruturas que executam blocos de instrução a depender de uma expressão booleana.
"""

### Vamos começar estudando a condicional if 

"""
    O condicional if é a principal das estruturas.
    Essa estrutura executa um bloco de código se determinada expressao booleana for verdadeira. 

    Sintaxe do if: 

    if(expressao): 
        ## algum bloco de código a ser executado caso expressao seja verdadeira

"""
### A expressão mais simples é a constante True. Como diz o proprio nome, é uma expressão que é sempre verdadeira.

## Exemplo 

if (True): 
    print("A expressão é verdadeira!")

### Analogamente, temos a expressão False

if (False):
    print("Esssa expressão é falsa!")

"""
    Identação: 

    Em outras linguagens, os blocos das estruturas condicionais são delimitados por {}
    Para delimitar o bloco em Python utilizamos : e indentamos por TAB o bloco a ser excecutado. 
    Isso torna o python uma linguagem indentada, sendo necessário se atendar ao espaçamento dos comandos em relação ao começa da linha. 

""" 

if (True): 
    print("A expressão é verdadeira")
    print("Não é mesmo?")

    if(True): 
        print("If encadeado")

if (False): 
    print("Esse nunca será executado")

print("Isso será sempre executado pois está em outro bloco.")

"""
Expressões Lógicas: 

O verdadeiro poder das estruturas condicionais é a possibilidade de criarmos nossas próprias expressões lógicas
a serem avaliadas. Para isso, fazemos uso do operadores de comparação. 

Operadores de comparação: 

Os operadores de comparação possuem uma sintaxe parecida com a de operadores aritméticos: 
            valor1 OPERADOR valor2

Operador            Descrrição

== Igual                Checa se o valo1 é igual ao valor2
!= Diferente            Chega se o valor1 é diferente ao valor2
> Maior que             Checa se o valor1 é maior que o valor2
< Menor que             Checa se o valor1 é menor que o valor2
>=Maior ou igual que    Checa se o valor1 é maior ou igual que o valor2
<=Menor ou igual que    Checa se o valor1 é menor ou igual que o valor2
"""
#Exemplos 

if ("bianca">"ana"):
    print("Funciona para definir ordem alfabética")

print("brianca">"ana")

if(2 >=1):
    print("2 é maior que 1")

if(5 == 5): 
    print("5 é igual a 5")

if(5 == 2): 
    print("5 é igual a 2")

"""
    Além dos operadores de comparação, podemos fazer uso de operadores lógicos para construir nossas expressões. 
    Esses operadores atuam entre duas expressões lógicas.  

    Operador                            Operação
    <expr1> and <expr2> "E"             Retorna verdadeiro se ambas expressões forem verdadeiras
    <expr1> or <expr2>  "OU"            Retorna verdadeiro se pelo menos uma das expressões for verdadeira
    not <expr1>         "NÃO"           Retorna a negação da expressão

    Podemos visualizar esses operadores por meio da tabela verdade: 
 
 
    Valores Operador and  Operador or

        0 0         0              0
        0 1         0              1
        1 0         0              1
        1 1         1              1
"""
expressao = 4 > 3 and 3 > 2 and 2 > 1
expressao2 = 5 > 10 or 3 > 2
expressao3 = 5 > 10 and 3 > 2

#print (expressao)
#print(type(expressao))


if (expressao):
    print("A expressao 1 é verdadeira!")

if (expressao2): 
    print("A expressao 2 é verdadeira")

if (expressao3): 
    print("Expressao 3 é verdadeira")

if(not expressao3): 
    print("A expressao 3 não é verdadeira")



