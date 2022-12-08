"""
A estrutura condicional final a ser estudada é o else. Ao contrário das outras estruturas, essa ferramenta não precisa de uma
expressão em sua sintaxe, porque só será executada quando todos os ifs e elfis tiverem falhado.
"""

numero = int(input("Qual o número?"))

if(numero>=100): 
    print(f"O número {numero} é maior que ou igual a 100")
elif(numero >= 50):
    print(f"O número {numero} é maior ou igual a 50")
elif(numero >= 10): 
    print(f"O número {numero} é maior ou igual a 10 mas menor que 50")
else: 
    print(f"O número {numero} é menor que 10")