#!/usr/bin/python3
################################## AUTOR #########################################
# Data: 16.11.2021                                                               #
# Author: Jefferson Ruiz                                                         #
# Email: jefferson.ruiz@outlook.com                                              #
# Repositorio: https://github.com/JeffersonARuiz/Zabbix_Grafana_AppleStore       #
# Descrição: Script que verifica/extrai as informações da página da Apple Store  #
# Versão: 1.0                                                                    #
##################################################################################


import sys
import requests
import re
from bs4 import BeautifulSoup

#URL da AppleStore Brasil.
URL_BASE = "https://apps.apple.com/br/app/"

#Exemplo de USO --> .appstore.ph nome-do-app ID09090909

if __name__ == '__main__':
    
    if len(sys.argv) < 3:
        print("Necessário informar três parametros:")
        print("1 - Nome do App na Apple Store Brasil. ")
        print("2 - ID do App na Apple Store Brasil.")
        print("3 - Tipo de verificação [ Nota | Versao | Avaliacoes | Debug ].")

        sys.exit(1)

    else: 

        #Salvando os parametros enviados nas variaveis 
        aplicacao_base = sys.argv[1]
        id_aplicacao = sys.argv[2]
        tipoVerificacao = sys.argv[3]

        #URL Formatada após inclusão de Parametros
        #print(URL_BASE + aplicacao_base + "/" + id_aplicacao) 

        URL_FORMATADA = URL_BASE +  aplicacao_base + "/" + id_aplicacao
        #print("URL => " + URL_FORMATADA)

        #Fazendo get na URL final e salvando na variável response
        response = requests.get(URL_FORMATADA)

        #Fazedo parse na resposta que retornou o conteudo em HTML
        site = BeautifulSoup(response.text, 'html.parser')

        #Obtendo o nome do App exibida na Apple Store
        titulo_aplicacao = site.find('h1', class_='product-header__title app-header__title').contents[0].strip()

        #Função que verifica a versão do App
        def VersaoApp():
          #Obtendo a versão do App publciada na Apple Store e substituindo o texto Versão por ""
          versao_app = site.find('p', class_='l-column small-6 medium-12 whats-new__latest__version').text.replace("Versão", "").strip()

          #Algumas apps possuem versão com prenteses Ex.: 4.1.1(2). abaixo estamos removendo os parenteses. 
          versao_app_final = re.sub('\([^)]*\)','',versao_app)

          return versao_app_final


        #Função que verifica a nota do App
        def NotaApp():
          #Obtendo a nova do App existente na Apple Store
          nota_app = site.find('span',class_='we-customer-ratings__averages__display').text.replace(',','.')

          return nota_app


        #Função que verifica a quantidade de avaliações que o APP Teve
        def AvaliacoesApp():

          #Obtendo o total de avaliações do App
          qtdAvaliacoes = site.find('div', class_='we-customer-ratings__count small-hide medium-show').text.replace(' avaliações','').strip()

          #verificando se a  quantidade de avaliações é superior a 999, quando temos mais de 1000 avaliações existe a string "mil" no valor (ex.: 245,3 mil)  para exibir numeração correta (multiplicar por mil).
          verificaTotal = qtdAvaliacoes.find("mil")

          #verifica se a quantidade de avaliações é superior a 999999, quando temos mais de 1 milhão de avaliações existe a tring "mi"no valor (ex: 5.8 mi) para exibir a numeração correta (multiplicar por 1 milhao)
          verificaTotalMilhao = qtdAvaliacoes.find("mi")

          #Se encontrar a string, ira retornar um numero maior ou igual a zero, caso contrário  ira retornar -1, que é quando a string não foi identificada. 
          if(verificaTotal >= 0):

             #obtendo o valor e substituindo a palavra "mil" do valor.
             totalNumerico = qtdAvaliacoes.replace(' mil','').replace(',','.').strip()

             #convertendo o numero de avaliacao de milhares pata inteiro.
             totalAvaliacoes = float(totalNumerico) * 1000

             return totalAvaliacoes

          else:

             if (verificaTotalMilhao >= 0):

               #obtendo o valor e substituindo a palavra "mi"do valor.
               totalNumericoMilhao = qtdAvaliacoes.replace(' mi','').replace(',','.').strip()

               #convertendo o numero de avaliacoes de milhoes para inteiro.
               totalAvaliacoes = float(totalNumericoMilhao) * 1000000

               return totalAvaliacoes

             else:

               #retornando o valor total de avaliações
               return qtdAvaliacoes

        #Função para obter a quantidade de avaliações do App na Loja.
        if tipoVerificacao == 'Avaliacoes':
            
            #Chamando a função que verifica a quantidade de avaliações do App
            quantidade = AvaliacoesApp()
            #imprimindo a Nota do App.
            print(int(quantidade))

        #Função para obter a NOTA do App na Loja.
        if tipoVerificacao == 'Nota':
            #Chamando a função que verifica a versão do App
            nota = NotaApp()
            #imprimindo a Nota do App.
            print(float(nota))

        #Função para obter a Versão do App na Loja.
        if tipoVerificacao == 'Versao':

            versao = VersaoApp()

            print(versao)

        #Função DEBUG que retorna todas as informações (Nota, Versão, Quantidade de Avaliações) do APP.
        if tipoVerificacao == 'Debug':

          nota = NotaApp()
          versao = VersaoApp()
          quantidade = AvaliacoesApp()

          print("App: " +  titulo_aplicacao + " | Versao: " + versao + " | Nota App Store: " + str(nota) + " | Qtd. Avaliações: " + str(quantidade) + "")

