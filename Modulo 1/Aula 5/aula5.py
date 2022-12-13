"""
    Aula 5: Funções

    Uma função é um conjunto de instruções que recebe argumentos de entrada e podem ou nao produzir uma saida. 
    Toda função é chamada pelo seu nome e com parênteses. Dentro dos parênteses, passamos os valores de entrada
    que a função requer. 

    Já falamos de várias funções até então. Agora vamos aprender a criá-la.
"""

"""
    Definindo funções: 

    - O nome de uma função deve ser algo significativo e indicar o que será feito de modo claro. 
    - Evite abreviar nomes. Ex. calcDtDiff não é um bom nome para uma função que calcula a diferença dentre duas datas. 
"""
## algumaFuncaoDoPython <- CamelCase (Utilizamos para criação de classes) - Geralmente em C++ etc escrevemos nome da função assim
## alguma_função_do_python <- Snake Case (Utilizamos para nome de função)

def dizer_ola():
    #Varios comandos podem estar nessa função
    print("Olá")
dizer_ola()


def dizer_ola(nome):
    print(f"Olá {nome}")

dizer_ola("Alessa")

def somar_numeros(a,b):
    print(a+b)

somar_numeros(4,6)
somar_numeros(6,7)

nome = input("Digite seu nome: ")
dizer_ola(nome)

"""
    Valores padrão: 
    Podemos atribuir valores padrão a nossos argumentos da função, tornando-os opcionais a quem estiver invocando a função. 

    É muito útil quando saber que esses parâmetros possuem certa definição. Por exemplo, podemos criar uma função que verifica
    se uma pessoa tem idade para dirigir ou não, dada a idade que é permitido dirigir em cada pais. 

"""
## return

def somar_numeros(a,b): 
    resultado = a +b
    return resultado # a variavel resultado só existe dentro da execução da função

resultado_da_funcao = somar_numeros(5,6)
print(resultado_da_funcao)

retorno1 = somar_numeros(5,6)
retorno2 = somar_numeros(10,12)

retorno3 = somar_numeros(retorno1, retorno2)
print(retorno3)

print(type(somar_numeros(5,6)))


## Argumentos posicionais -> a ordem importa

def dizer_ola(nome, idade, sistema): 
    texto = f" Olá {nome}, de {idade} anos. Bem-vindo ao sistema {sistema}"
    return texto

retorno_da_funcao = dizer_ola("Alessa","25","SuperApp")
print(retorno_da_funcao)

print(dizer_ola(sistema="superApp", nome="Alessa", idade="25"))

def checa_idade(idade):
    if(idade>=18): 
        return True
    else:
        return False

idade= 20
if(checa_idade(idade)):
    print("Pode dirigir")
else:
    print("Não pode dirigir")


def checa_idade(idade, idade_minima = 18): 
    if idade >= idade_minima: 
        return "Pode dirigir"
    else:
        return "Não pode dirigir"

print(checa_idade(20)) # nesse o argumento padrao idade_minima = 18
print(checa_idade(20, 21)) # nesse caso idade_minima = 21


def checa_idade_bool(idade, idade_minima=18):
    if idade>= idade_minima: 
        return True
    else: 
        return False

idade = 15
if checa_idade_bool(idade):
    print("Pode dirigir - bool")
else: 
    print("Não pode dirigir - bool")

## Exercícios: 

## Função para calcular o máximo de três números(criando uma função auxiliar que calcular o máximo de dois números).
## Recebe 3 números e retorna o maior. 

"""
    max2(a,b)
    max3(a,b,c)
    k = max2(a,b)
    return max2(k,c)
"""

## Função que recebe como argumento uma lista e retorna uma lista com os valores unicos da lista original
"""
    lista_unica([1,1,2,2,5,5,8,9]) = [1,2,5,8,9]
    dica: crie uma lista auxiliar e adicione os numeros nao repeditos,
    retorne a lista auxiliar
"""

## Função que recebe uma string e chega se é um palindromo ou não

"""
    Como inverter listas? Faça o mesmo para strings inverter e ver se é igual. 

"""

## Desafio: função que recebe um inteiro n e printa as n primeiras linhas do triangulo e pascal. Dica funçao zip. 