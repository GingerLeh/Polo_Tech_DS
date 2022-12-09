"""
Faça um programa que imprima a seguinte saida:

1 ----- 99

2 ----- 98

3 ----- 97

..

..

..

98 ---- 2

99---- 1
"""
for i in range(1, 100):
    print(f"{i} ----- {(100-i)}")
    

