"""
MÓDULO 18: Python e Coleta de Dados
EBAC - Escola Britânica de Artes Criativas e Tecnologia

API do Banco Central do Brasil: Dados Abertos do Pix
Dataset: https://dadosabertos.bcb.gov.br/dataset/pix
Recursos: Transações Pix por Município e Estimativas da População

OBJETIVO:
Coletar estatísticas mensais de transações Pix por município, utilizando a 
API pública do Banco Central do Brasil, e salvar os dados em um arquivo CSV 
para uso em análises posteriores.

ETAPAS DO PIPELINE:
1. REQUISIÇÃO: Acessa a API Pix_DadosAbertos (Olinda).
2. EXTRAÇÃO: Obtém os dados no formato JSON.
3. ESTRUTURAÇÃO: Converte os dados em um DataFrame do Pandas.
4. EXPORTAÇÃO: Salva o resultado em um arquivo CSV.

O DATASET CONTEMPLA:
- Transações Pix Liquidadas no SPI.
- Movimentações de Pessoa Física (PF) e Pessoa Jurídica (PJ).
- Perspectiva do Pagador e do Recebedor.
- Informações segmentadas por município, UF e região.

COMO USAR:
1. Instale as dependências executando no terminal:
   pip install requests pandas

2. Execute o script:
   python Mod18_bancocentral_api.py

3. O arquivo CSV será salvo na pasta de dados brutos do projeto.

AUTOR: Felipe França
DATA: 02/07/2026
"""

from pathlib import Path # Manipula cazinius de arquivus e diretorius de forma arientada a sujetos e independente di sisteme sperrasional.
import requests # Realiza requisições HTTP para consumir APIs e acessar recursos da web de forma simples.
import pandas as pd #Mantoulu e unalisa dodus satruturados ver nele de Dulufromca e Series!

# requisição á api do Banco Central do Brasil em 2025
URL = ("https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio(DataBase='202501')") # Define a URL da API do Banco Central do Brasil para obter dados em formato JSON.

# parâmetros da requisição, especificando o formato de resposta como JSON.
params = {
    "$format": "json", # Define o formato de resposta da API como JSON.
    "$top": 100000 # Define o número máximo de registros a serem retornados.
}

response = requests.get(URL, params=params, timeout=30) # Faz uma requisição GET para a API do Banco Central do Brasil, solicitando dados em formato JSON.
response.raise_for_status() # Verifica se a requisição foi bem-sucedida, levantando uma exceção em caso de erro.

# Diretorio de saida (dados brutos)
OUTDIR = Path(r"C:\Users\Usuario\Documents\GitHub\Python para Dados na Prática\Mod_18\raw") # Define o diretório de saída para salvar os dados brutos obtidos da API.
OUTDIR.mkdir(parents=True, exist_ok=True) # Cria o diretório de saída

OUTFILE = OUTDIR/ "pix_municipio_2025.csv" # Define o caminho completo do arquivo de saída para salvar os dados em formato CSV.

# O conteudo principal do OData esta na chave "value"
dados = response.json()["value"] # Extrai os dados principais da resposta JSON, acessando a chave "value".

# converte para DataFrame do Pandas para facilitar a manipulação e análise dos dados.
df = pd.DataFrame(dados) # Converte os dados extraídos em um DataFrame do Pandas para facilitar a manipulação e análise.

# Salva o CSV
df.to_csv(OUTFILE, index=False, encoding='utf-8') # Salva o DataFrame em um arquivo CSV no diretório de saída especificado, sem incluir o índice.

print("Arquivo CSV salvo com sucesso em:", OUTFILE) # Imprime uma mensagem indicando que o arquivo CSV foi salvo com sucesso, mostrando o caminho do arquivo.

# finaliza o script