"""
Em determinada universidade um estudante só pode realizar a prova final caso possua mais de 75% de presença.

Faça um programar que receba o número total de aulas dadas, a quantidade de aulas em que o aluno estava presente 
e imprima a porcentagem da frequência e se o aluno pode ou não realizar a prova final.
"""

aulas_dadas = int(input("Digite a quantidade de aulas dadas: "))
aulas_assistidas = int(input("Digite a quantidade de aulas assistidas pelo aluno: "))

porcentagem = (100 * aulas_assistidas) / aulas_dadas

if(porcentagem > 75):
    print(f"O aluno pode fazer a prova final, pois possui {porcentagem}% de presença")
else: 
    print(f"O aluno não poderá fazer a prova final, pois possui {porcentagem}% de presença")