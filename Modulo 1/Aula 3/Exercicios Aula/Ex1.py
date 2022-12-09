### Checar se um número é perfeito. Um número é perfeito se é igual a soma dos seus divisores positivos diferentes de ele
### mesmo. 6 é perfeito porque 1 + 2 + 3 = 6

num  = int (input("Insira o número: "))
soma = 0

for i in range(1, num//2+1):
    if num%i == 0: 
        soma+=i

if(soma == num): 
    print(f"O número {num} é perfeito")
else: 
    print(f"O número {num} não é perfeito")