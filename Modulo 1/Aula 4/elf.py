with open("input1.txt") as f:
    lines = [line.rstrip() for line in f]


n_calorias = 0
n_max_calorias = 0

for line in lines:
    if line == "":
        if (n_calorias > n_max_calorias):
            n_max_calorias = n_calorias
        n_calorias = 0
    else:
        n_calorias += int(line)

print(f"O número máximo de calorias é {n_max_calorias}")
