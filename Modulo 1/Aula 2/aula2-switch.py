"""
    Em linguagens de programação, uma instrução switch é um tipo de mecanismo
    de controle de seleção usado para permitir que o valor de uma variável ou 
    expressão altere o fluxo de controle da execução do programa. 

    Em JavaScript podemos escrever um switch statement da seguinte forma:

    switch(expression) {
        case x:
            ###code
            break;
        case y:
            ###code
            break;
        default:
            ##code block
    }

    Até a versão 3.10, o Python não tinha uma implementação de switch. Assim, se vc quisesse
    executar multiplos condicionais você teria que utilizar o elif da seguinte forma

"""

linguagem = "Python"
if linguagem == "Javascript": 
    print("Seja um desenvolvedor web")
elif linguagem == "PHP": 
    print("Seja um desenvolvedor backend")
elif linguagem == "Python": 
    print("Seja um cientista de dados")
elif linguagem == "Java": 
    print("Seja um desenvolvedor mobile")
else: 
    print("Não conheço essa linguagem")

"""
    A partir do 3.10 foram adicionadas ao python as seguintes keywords: match e case. Assim, 
    se tornou possivel implementar instruções swtich de forma mais limpa. 
"""

match linguagem: 
    case "Javascript": 
        print("web")
    case "Python": 
        print("Ciencia de dados")
    case _:
        print("nao conheço")


### Exercicio: 
# Faça um programa que retorne a quantidade de dias de um mês usando switch statement. 
# Obs: Considere os meses como sendo 1,2,3, ... 12