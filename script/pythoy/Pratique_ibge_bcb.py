

import requests
import pandas as pd

# Nota: Para salvar em parquet, você pode precisar instalar a biblioteca pyarrow
# !pip install pyarrow

# Fazendo a requisição na API de Localidades do IBGE
url_ibge = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
response_ibge = requests.get(url_ibge)

if response_ibge.status_code == 200:
    dados_ibge = response_ibge.json()
    df_ibge = pd.DataFrame(dados_ibge)
    print("Dados do IBGE carregados com sucesso!")
    print(df_ibge.head(3))
else:
    print(f"Erro ao acessar IBGE: {response_ibge.status_code}")



    # Fazendo a requisição na API do BCB (Cotação do Dólar em Jan/2024)
url_bcb = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='01-01-2024'&@dataFinalCotacao='01-31-2024'&$format=json"

response_bcb = requests.get(url_bcb)

if response_bcb.status_code == 200:
    # A API do BCB retorna os dados dentro da chave 'value'
    dados_bcb = response_bcb.json()['value']
    df_bcb = pd.DataFrame(dados_bcb)
    
    # Exibindo as primeiras linhas
    print("Dados do BCB carregados com sucesso!")
    print(df_bcb.head())
    
    # Salvando os dados brutos em CSV
    df_bcb.to_csv('bcb_tabela.csv', index=False)
    print("\nArquivo 'bcb_tabela.csv' salvo com sucesso!")
else:
    print(f"Erro ao acessar BCB: {response_bcb.status_code}")




    # Criando uma cópia para tratar os dados
df_tratado = df_bcb.copy()

# TRATAMENTO 1: Renomear colunas para o padrão snake_case
df_tratado = df_tratado.rename(columns={
    'cotacaoCompra': 'cotacao_compra',
    'cotacaoVenda': 'cotacao_venda',
    'dataHoraCotacao': 'data_hora_cotacao'
})

# TRATAMENTO 2: Converter a coluna de data (string) para o tipo datetime do Pandas
df_tratado['data_hora_cotacao'] = pd.to_datetime(df_tratado['data_hora_cotacao'])

# TRATAMENTO 3: Remover colunas desnecessárias (ex: tipoBoletim)
# df_tratado = df_tratado.drop(columns=['tipoBoletim'])

# VALIDAÇÃO DOS DADOS
print("--- VALIDAÇÃO DOS DADOS ---")
print("\n1. Verificação de Tipos (info):")
print(df_tratado.info())

print("\n2. Contagem de Valores Nulos:")
print(df_tratado.isnull().sum())

print("\n3. Contagem de Registros Duplicados:")
print(df_tratado.duplicated().sum())



# Salvando em CSV
df_tratado.to_csv('dados_tratados.csv', index=False)

# Salvando em Parquet (formato colunar altamente otimizado)
df_tratado.to_parquet('dados_tratados.parquet', index=False)

print("Arquivos 'dados_tratados.csv' e 'dados_tratados.parquet' salvos com sucesso!")