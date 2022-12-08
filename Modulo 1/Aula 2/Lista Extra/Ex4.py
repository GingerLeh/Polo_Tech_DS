"""
Uma escola possui o sistema de avalição que dependendo da nota obtidada o aluno 
recebe uma avaliação entre A, B, C, D, E e F a partir dos seguintes critérios:

Abaixo de 25: F
Maior ou igual a 25 e menor que 45: E
Maior ou igual a 45 e menor que 50: D
Maior ou igual a 50 e menor que 60: C
Maior ou igual a 60 e menor que 80: B
Maior ou igual a 80: A
Faça um programa que recebe do usuário a nota e imprima a avaliação.
"""

nota = float(input("Digite a nota do aluno: "))

if(nota < 25):
    print(f"Nota {nota} : F")
elif(nota >= 25 and nota < 45):
    print(f"Nota {nota} : E")
elif(nota >= 45 and nota < 50):
    print(f"Nota {nota} : D")
elif(nota >= 50 and nota < 60):
    print(f"Nota {nota} : C")
elif(nota >= 60 and nota < 80):
    print(f"Nota {nota} : B")
else: 
    print(f"Nota {nota} : A")

