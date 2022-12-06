print("########## Exercicio Futebol ##########")
time = input("Digite o nome do time:")
vitorias = int(input("Digite a quantidade de vitórias:"))
empates = int(input("Digite a quantidade de empates:"))
derrotas = int(input("Digite a quantidade de derrotas:"))

pvitorias = vitorias * 3
pempates = empates * 1 

print(f"\n\n\nO time {time} teve:")
print(f"{pvitorias} pontos com {vitorias} vitorias")
print(f"{pempates} pontos com {empates} empates")
print(f"E teve {derrotas}. derrotas")
print(f"Total de pontos: {pvitorias+pempates}")