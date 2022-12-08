"""
Uma loja de departamento dará um desconto de 10% caso o valor da compra seja maior que R$ 500.

Os itens disponíveis para compra são os seguintes:

Calça: R$ 70,00
Blusa: R$ 30,00
Casaco do de frio: R$ 150,00
Sapato: R$ 80,00
Faça um programa que receba a quantidade comprada de cada item e imprima o valor total a ser 
pago após a aplicação do desconto (se disponível).

"""

calca = 70
blusa = 30
casaco = 150
sapato = 80

qtd_calca = int(input("Quantas calças foram compradas?"))
qtd_blusa = int(input("Quantas blusas foram compradas?"))
qtd_casaco = int(input("Quantos casacos foram comprados?"))
qtd_sapato = int(input("Quantos sapatos foram comprados?"))

total_compra = qtd_calca * calca + qtd_blusa *blusa + qtd_casaco * casaco + qtd_sapato * sapato

if (total_compra > 500): 
    novo_valor = total_compra - total_compra * 0.10 
    print(f"Valor total da compra: {total_compra}")
    print(f"Valor total da compra com desconto de 10%: {novo_valor}")
else:
    print (f"Valor total da compra foi: {total_compra}")