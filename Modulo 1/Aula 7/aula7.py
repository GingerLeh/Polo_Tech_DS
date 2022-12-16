#https://pypi.org -> local onde ficam os pacotes do python
#https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments

"""
    - Primeiro ver a versão ou ver se está instalado: pip -V
"""

"""
    Para instalação de pacotes:  pip install nome_do_pacote
    Exemplo: 
    - pip install pandas
    - pip install numpy
"""
"""
    Criação de arquivo requirements.txt -> aquivo com os pacotes necessarios para o projeto
    Exemplo do que escrever no arquivo: 

    pandas == 5.2.0

    Depois: 

    pip install -r requirements.txt
    pip freeze -> mostra os pacotes instalados no ambiente

"""

"""
    Virtualização de ambientes: 
    - para instalar: pip install virtualvenv
    - Comando: virtualenv nome_da_virtualenv
    - Uma vez criado seu ambiente virtual, você deve ativá-lo.
        - Comando: nome_da_virtualenv/Scripts/Activate
    - Para desativar um ambiente virtual:
        - Comando: deactivate
"""

"""
    Importação de arquivos: 

    - Importar e instalar a biblioteca requests.
    - pip install requests
"""
import requests 

response = requests.get('https://google.com')
print("Status: ", response.status_code)


