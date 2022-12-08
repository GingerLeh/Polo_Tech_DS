"""
Escreva um programa que receba a largura e o comprimento dos lados de um retângulo e indique se é um quadrado ou não.

Além disso, imprima seu perimetro e sua área.

Lembrando que para um retângulo de lados $a$ e $b$ a área e o perimetro são dados por:

p=2*a+2*b
A=a*b

"""

largura = float(input("Digite a largura do retangulo:"))
comprimento = float(input("Digite o comprimento do retangulo:"))

if(largura == comprimento): 
    print("O retangulo é um quadrado!")

perimetro = 2*largura + 2 *comprimento
area = comprimento * largura 

print(f"O perimetro do retangulo é: {perimetro}")
print(f"A área do retangulo é: {area}")