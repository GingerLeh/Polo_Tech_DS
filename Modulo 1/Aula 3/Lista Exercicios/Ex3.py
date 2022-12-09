"""
Faça um programa que leia da entrada padrão três números a, b, c e imprima quantos números entre 
a e b (não incluso) são divisíveis por c.
"""

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero maior que o primeiro: "))
c = int(input("Digite outro numero: "))

contador=0
for i in range(a+1, b): 
    if i%c==0: 
        contador+=1
        print(f"{i} é divisivel por {c}")
print(f"\nTotal de números divisiveis por {c} no intervalo {a} - {b}: {contador}")