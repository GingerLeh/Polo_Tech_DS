"""
A distância euclideana entre dois pontos é dada pela seguinte equação:


d=√(x1−x2)^2+(y1−y2)^2

Monte um código onde irá receber os valores de $x_1$, $y_1$, $x_2$ e $y_2$ em metros 
(podendo ser valores decimais) e retorne o valor da distância euclidiana em metros também.
"""

import math
x1 = float(input("Digite o x1 "))
x2 = float(input("Digite o x2 "))
y1 = float(input("Digite o y1 "))
y2 = float(input("Digite o y2 "))

distancia = math.sqrt(
    (x1-x2)**2 + (y1+y2)**2
)
print(f"Distancia euclidiana: {distancia}")