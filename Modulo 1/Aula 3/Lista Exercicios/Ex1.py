"""
Faça um programa que ache os números que são divisíveis por 7 e múltiplos de 5 entre 1500 e 2700 (ambos inclusos).
"""

for i in range(1500, 2701,1): 
    if i%7 == 0: 
        print(f"Numeros divisiveis por 7: {i}")

print("\n============================================\n")

for i in range(1500, 2701,5): 
    print(f"Multiplos de 5: {i}")
