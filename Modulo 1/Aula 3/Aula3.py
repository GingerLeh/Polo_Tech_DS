# Açucar sintático:  https://pt.wikipedia.org/wiki/A%C3%A7%C3%BAcar_sint%C3%A1tico

"""
    Laços de repetição - Introdução

    Em quase todas as aplicações, precisaremos que um programa execute o mesmo conjunto de instruções
    diversas vezes. Para evitar que seja necessário escrever o mesmo bloco de código diversas vezes as linguagens de programação
    possuem estruturas chamadas de laços de repetição.

    Dentro dessas estruturas, cada vez que executamos uma das instruções estamos realizando uma iteração. 
    A quantidade iterações depende de expressões condicionais.
"""

"""
    Laço Condicional: While

    Se quisermos atrelar a repetição de um código a uma expressão condicional (como no if), fazemos uso do while. 

    O while executará o conjunto de instruções dentro do seu bloco enquanto a condição especificada for verdadeira. 
    Sua sintaxe é a seguinte: 

    while (expressao): 
        #bloco de codigo
    
"""

### Por exemplo, se quisermos executar um comando 5 vezes: 
i = 0
while i<5: 
    print (f"i={i}")
    i+=1

# Se eu quero executar o comando n vezes faço o seguinte: 

"""
    i = 0 
    while i < n:
        #codigo 
        i += 1
"""

### Também podemos utilizar o while para validarmos continuamente
### os dados que o usuário inseriu até que um valor válido seja providenciado. 

idade = 0 
while idade < 18: 
    idade = int(input("Qual sua idade (mínimo 18 anos)?"))
print(f"Idade = {idade}")

"""
    Laços com contador numérico: for

    Quando sabemos previamente a quantidade de iterações que serão necessárias podemos utilizar uma outra destrutura 
    denominada for. Podemos reescrever o exemplo acima da seguinte forma:
"""

for i in range(5): 
    print(f"for i = {i}")

## range(0,n,1) = range(n)
for i in range(10,-1,-1): 
    print(f"for i = {i}")

"""
    A função range(n) cria um iterador numérico. Essa função possui uma série de parametros como: 
        inicio, fim, passo. 
    A estrutura for também possui uma sintaxe for .... in, mas veremos isso quando falarmos de listas.
"""

"""
    Controle de Fluxo

    É possivel pularmos iterações do while e do for ou até mesmo para a repetição antes que a condição 
    de parada seja satisfeita.
    Pulando iterações com continue: 

"""

i = 0
while i <10:

    if(i%2==0):
        continue
    print(f"Número {i}")
    i+=1

for i in range(0, 11): 
    if(i%2==0):
        continue
    print(f"Número no for: {i}")

existe_pulado = False
for i in range(0, 11): 
    if i == 7: 
        existe_pulado = True
        pulado = i
        continue
    print(f"Numero no for {i}")
print(pulado)

if (existe_pulado): 
    print(pulado)
else: 
    print("Não existe pulado")

"""
    Parando laços com break: Vamos fazer um script que peço nomes sequencialmente até que o usuário pressione o ENTER sem 
    preencher nada. 
"""

print("Escreva os nomes (pressione ENTER para parar")

while True: 
    nome = input(">Digite um nome: ")
    if nome == "": 
        break
    print(f"Inserindo {nome}")
print("Saindo...")





