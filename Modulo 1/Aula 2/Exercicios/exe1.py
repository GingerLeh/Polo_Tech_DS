"""
Crie um código que receba o nome do aluno, o ano de nascimento, 
o dia de hoje e a cidade onde mora. E o programa deve retornar o nome, 
a idade em 2022, quantos dias faltam para o Natal (25), 
quantos dias que faltam para a véspera de ano novo (31) e a cidade.
"""

import datetime

nome = input("Digite o nome do aluno: ")
ano_nascimento = int(input("Digite o ano do nascimento do aluno: "))
cidade = input("Digite a cidade do aluno: ")

natal = datetime.datetime(2022,12,25)
vespera = datetime.datetime(2022,12,31)
hoje = datetime.datetime(2022,12,6)

idade =  2022 -ano_nascimento
dias_ate_natal = natal-hoje
dias_ate_vespera = vespera -hoje

print(f"Nome do aluno: {nome}")
print(f"Idade do aluno: {idade}")
print(f"Dias até o natal: {dias_ate_natal}")
print(f"Dias até a vespera de ano novo: {dias_ate_vespera}")
print(f"Cidade: {cidade}")