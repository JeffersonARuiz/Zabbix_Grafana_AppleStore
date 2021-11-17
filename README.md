# Tamplate e Dashboard Zabbix e Grafana

[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/JeffersonARuiz)](https://github.com/JeffersonARuiz) [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://br.linkedin.com/in/jeffersonruizalvarezruiz)](https://br.linkedin.com/in/jeffersonruizalvarezruiz)

Acompanhe as Avaliações, Notas e Versionamento dos seus Apps publicados na Apple Store através do Zabbix e Grafana.

<img src="https://github.com/JeffersonARuiz/Zabbix_Grafana_AppleStore/blob/main/Dashboard.png" />

# Requisitos

  - Zabbix 4 ou Superior
  - Grafana 8 ou Superior
  - Python 3
  - Python | BeautifulSoup
  - Python | Requests
  - Integração Grafana e Zabbix - https://alexanderzobnin.github.io/grafana-zabbix/installation/ 

# Script Python | Arquivos

<strong>Arquivo 01:</strong> <i><b>applestore.py</b></i> - Arquivo utilizado no “protótipo de Itens” do Zabbix para coletar as informações dos Apps na Apple Store.

<strong>Arquivo 02:</strong> <i><b>DiscoveryAppStore.py</b></i> - Arquivo utilizado na regra de descoberta do Zabbix para coletar as informações dos Apps na Apple Store.

<strong>Arquivo 03:</strong> <i><b>AppleStore.list</b></i> - Arquivo utilizado pelo Script “DiscoveryAppStore.py” para descobrir cada um dos itens existentes na lista assim como incluir/ativar/desativar itens a serem monitorados.

O Arquivo <b>AppleStore.list</b> esta estruturado com quatro parâmetros, separados por  “;” (Ponto e virgula), conforme detalhe abaixo:

<b>1º Parâmetro =</b> Status : Se for 1 o APP está Ativo para ser monitorado pelo Zabbix, se for 0 (Zero) o App está inativo para monitoração.

<b>2º Parâmetro =</b> Nome da aplicação : O Nome da aplicação varia de acordo com a URL da Apple Store, neste caso seria “microsoft-onedrive”

<b>3º Parâmetro =</b> ID da aplicação :  O ID da aplicação varia de acordo com a URL da Apple Store, neste caso seria “id477537958”, conforme URL de exemplo abaixo

      https://apps.apple.com/br/app/microsoft-onedrive/id477537958 

**4º Parâmetro =** Label da Aplicação : Este é o nome que será exibido no monitor dentro do Zabbix, ficando a critério no momento da criação, por exemplo, One Drive ou OneDrive ou ainda, Driver Microsoft.
  
  **OBS.:**  *Sempre que você precisar incluir uma nova aplicação na monitoria, é necessário editar o arquivo **Applestore.list** e inserir os parâmetros da aplicação.*
  
  
# IMPORTANDO OS TEMPLATES NO ZABBIX

**Passo 01**: Copiar os 3 arquivos ( **applestore.py** | **DiscoveryAppStore.py** | **AppleStore.list**) para o diretório *“externalscripts”* do Zabbix. Esse diretório é variável dependendo da versão do sistema operacional onde o Zabbix foi instalado, no meu caso os arquivos foram copiados para o diretório */usr/lib/zabbix/externalscripts*

**Passo 02**: Aplicar as permissões e mudar o Owner para os três arquivos que acabamos de copiar para o servidor do Zabbix, conforme comandos abaixo.
			*Mudança do Owner*:  chown zabbix:zabbix *nome do arquivo.py*
			*Permissões*: chmod 755 *nome_do_arquivo.py*

**Passo 03**: Neste passo, vamos importar o template no Zabbix, sendo assim, Acesse  a console do Zabbix, clicar no menu **CONFIGURAÇÃO**, em seguida clicar em **TEMPLATES**, ao abrir a tela, clique no botão **IMPORTAR**, localizado no canto superior direito da tela e importe o arquivo **TLPT_ZABBIX_APPS_APPLESTORE.json**.

**Passo 04**: Agora faremos a importação do HOST no Zabbix. Acesse  a console do Zabbix, clicar no menu  **CONFIGURAÇÃO**, em seguida clicar em **HOSTS**, ao abrir a tela, clique no botão **IMPORTAR**, localizado no canto superior direito da tela  e importe o arquivo **HOST_TLPT_ZABBIX_APP_APPLESTORE.json**.

*Pronto, toda a configuração necessária ja esta executada no Zabbix, aguarde o tempo de 5 minutos que esta parametrizado no Template para que a regra de descoberta execute os scripts e exiba as aplicações que estão parametrizadas no arquivo AppleStore.list.*

# IMPORTANDO OS TEMPLATES NO GRAFANA

  **IMPORTANTE**:  Para que o a importação do template funcione, a integração com o Zabbix com o Grafana ja deve ter sido executada. 


  **Passo 01**: Copiar a pasta “AppleStore” que contem todas as imagens dos APPs monitorados para o servidor do Grafana e colar a pasta completa no caminho “grafana\public\img”

  **Passo 02**: Acessar o Grafana com um usuário com permissão para importação de Dashboard, clicar no ícone **“+”** localizado no menu do Grafana em seguida clicar em **IMPORT** 

  **Passo 03**: Ao carregar a tela, clicar no botão **UPLOAD JSON FILE** e localize o arquivo **DASHBOARD_GRAFANA.json** em seu computador.

  **Passo 04**: Selecione a pasta (Folder) que deseja salvar o Dashboard da Apple Store, dentro do seu Grafana.

  **Passo 05**: Ao carregar a tela de Importação, selecione o Data Source do Zabbix e clique no Botão **IMPORT**
          
  Pronto, após clicar no botão Import, caso o processo tenha sido executado de forma correta, você será direcionado para o Dashboard com os dados de monitoração das APPs.
  
  **IMPORTANTE**: Para acelerar a integração e atualização dos dados no Grafana, você pode efetuar o restar do serviço do Grafana, caso não queira reiniciar o Grafana, aguarde de 5 a 10 minutos para a sincronização dos dados entre o Zabbix e Grafana.

