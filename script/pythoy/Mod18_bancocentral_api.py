



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