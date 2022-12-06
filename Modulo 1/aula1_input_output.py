## ler um dado da entrada padrão

nome = input ("Qual seu nome?")
idade = input ("Qual sua idade?")
altura = input ("Qual sua altura?")
print("Olá " + nome)
print("Idade: " + idade)
print("Altura: " + altura)

### Outras formas de printar
print("Olá",nome,"tudo bem?") #coloca espaços automaticamente
print("Olá",nome,"tudo bem?",sep="**")

## Usando f-string
print(f"Olá {nome},tudo bem?") ## as chaves funcionam como placeholder

### Exercicio 1 

"""
    Crie um programa que receba o nome de um time de futebol, o número de vitórias, o número de derrotas e o número de 
    empates, e imprima a quantidade total de pontos.

    Vitória: Recebe 3 pontos.
    Derrota: Recebe 0 pontos.
    Empate: Recebe 1 pontos.  

"""