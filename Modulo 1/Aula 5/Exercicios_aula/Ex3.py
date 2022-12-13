"""
    Função que recebe uma string e chega se é um palindromo ou não
"""

def palindromo(string):
    string = string.upper()
    reverse = string[::-1].upper()
    
    if reverse == string:
        return "É palindromo"
    else:
        return "Não é palindromo"
print(palindromo("Anna"))