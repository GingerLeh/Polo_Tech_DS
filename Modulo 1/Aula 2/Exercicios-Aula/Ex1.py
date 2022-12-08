"""
Uma companhia decidiu dar um bônus de 5% a todos os funcionários que possuem mais de 5 anos de serviço.
Escreva um programa que receba do usuário o salário do funcionário, o tempo total de serviço e o bônus calculado.
"""
salario = float(input("Digite o salario: "))
tempo = int(input("Digite o tempo de serviço: "))

if(tempo>5): 
    novo_salario = salario * 0.05 + salario
else: 
    novo_salario = 0

print(f"O salario antigo era {salario}")
print(f"O tempo de trabalho é {tempo}")
print(f"O bonus calculado é {novo_salario}")
print(f"Novo salario: {novo_salario}")