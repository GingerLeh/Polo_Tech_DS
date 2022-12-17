import requests
import csv 

url = "https://raw.githubusercontent.com/likury/921/main/%5EIXIC.csv"
data =  requests.get(url)

text = data.text

lines = data.text.splitlines()


conteudo = []

# for linha in lines: 
#     linha_sep = linha.split(sep=",")
#     print(linha_sep)
#     conteudo.append(linha_sep)

# print(conteudo)
# print(conteudo[0])
# def acessa_conteudo(n,col, conteudo):
#     if col == "Date": 
#         return conteudo[n][0]
#     elif col == "Open":
#         return conteudo[n][1]
#     elif col == "High": 
#         return conteudo[n][2]
#     elif col == "Low":
#         return conteudo[n][3]
#     elif col == "Close":
#         return conteudo[n][4]
#     elif col == "Adj Close":
#         return conteudo[n][5]
#     elif col == "Volume": 
#         return conteudo[n][6]
#     else: 
#         return -1

# print(acessa_conteudo(1,"Date",conteudo))
reader = csv.reader(lines)

for linha in reader:
    print(linha)
