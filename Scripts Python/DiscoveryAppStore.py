#!/usr/bin/python3
################################## AUTOR #########################################
# Data: 16.11.2021                                                               #
# Author: Jefferson Ruiz                                                         #
# Email: jefferson.ruiz@outlook.com                                              #
# Repositorio: https://github.com/JeffersonARuiz/Zabbix_Grafana_AppleStore       #
# Descrição: Script para percorrer a lista de APPs a ser monitoradas (Discovery) #
#            na ferramenta Zabbix.                                               #
# Versão: 1.0                                                                    #
##################################################################################


import os
import sys
import json
FILE = "/usr/lib/zabbix/externalscripts/Applestore.list"

#Verificando se o Arquivo (Applestore.list) existe no diretori informado na variável "FILE"
if not os.path.isfile(FILE):
    print("File not found")
    sys.exit()

# Abrindo o Arquivo (Applestore.list) em modo leitura. 
file = open(FILE, "r")

#Criando um Array vazio para armazenar os objetos json. 
data = {
    "data": []
}

#Executando Loop em todas as linhas do Arquivo (Applestore.list) 
for line in file.readlines():
    #Executando Split de cada um dos campos do arquivo que estão separados por ";" (Ponto e Virgula)
    line_data = line.rstrip().split(';')
    
    #Validando se o parametro de Status (Primeiro parametro do arquivo) é 1 (Ativo) ou 0(Inativo). Se for 1, insere no Array "data"
    if line_data[0] == '1':
        dic = {"{#APP_NOME}": line_data[1], "{#APP_ID}": line_data[2]}
        data['data'].append(dic)
#Retornando o Json formatado para o Zabbix (Discovery) 
print(json.dumps(data))
