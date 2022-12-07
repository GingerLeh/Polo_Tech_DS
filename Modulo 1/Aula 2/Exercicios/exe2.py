"""
Crie um código onde irá receber do usuário a nota de 5 provas realizadas (as notas variam entre 0 e 10 
podendo ser um número decimal) e retorne o valor da média nas provas.
"""

prova_1 = float(input("Digite a primeira nota: "))
prova_2 = float(input("Digite a segunda nota: "))
prova_3 = float(input("Digite a terceira nota: "))
prova_4 = float(input("Digite a quarta nota: "))
prova_5 = float(input("Digite a quinta nota: "))


total = prova_1 + prova_2 + prova_3 + prova_4 + prova_5
media = total/5

print(f"A média total foi: {media}")