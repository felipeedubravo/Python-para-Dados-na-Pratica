"""
MÓDULO 18: Python e Coleta de Dados
EBAC - Escola Britânica de Artes Criativas e Tecnologia

APIs Públicas: IBGE (Localidades) e Banco Central do Brasil (PTAX)

OBJETIVO:
Realizar a extração, tratamento e validação de dados de duas APIs públicas 
diferentes, exportando os resultados estruturados para os formatos CSV e Parquet.

ETAPAS DO PIPELINE:
1. REQUISIÇÃO E EXTRAÇÃO: Consome os endpoints públicos do IBGE e do BCB.
2. ESTRUTURAÇÃO: Carrega os dados JSON em DataFrames do Pandas.
3. TRATAMENTO: Padroniza a nomenclatura das colunas e converte tipos de dados (Datas).
4. VALIDAÇÃO: Checa valores nulos, duplicatas e integridade estrutural.
5. EXPORTAÇÃO: Salva os dados limpos localmente em formato CSV e Parquet.

COMO USAR:
1. Instale as dependências executando no terminal:
   pip install requests pandas pyarrow

2. Execute o script:
   python Pratique_ibge_bcb.py

AUTOR: Felipe França
DATA: 02/07/2026
"""

from pathlib import Path # Manipula caminhos de arquivos de forma segura em qualquer sistema operacional.
import requests          # Realiza requisições HTTP para consumir as APIs públicas.
import pandas as pd      # Manipula, limpa e analisa os dados tabulares.

# ==========================================
# CONFIGURAÇÃO DE DIRETÓRIOS
# ==========================================
# Define o diretório de saída exato na sua máquina local
OUTDIR = Path(r"C:\Users\Usuario\Documents\GitHub\Python para Dados na Prática\Mod_18\raw")
OUTDIR.mkdir(parents=True, exist_ok=True) # Cria a pasta automaticamente se ela não existir

# ==========================================
# PARTE 1: EXTRAÇÃO DE DADOS DO IBGE
# ==========================================
print("Iniciando extração do IBGE...")
url_ibge = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

response_ibge = requests.get(url_ibge, timeout=30)

if response_ibge.status_code == 200:
    dados_ibge = response_ibge.json()
    df_ibge = pd.DataFrame(dados_ibge)
    print("✓ Dados do IBGE carregados com sucesso!\n")
    print(df_ibge.head(3))
    print("-" * 50)
else:
    print(f"Erro ao acessar IBGE. Código de status: {response_ibge.status_code}")

# ==========================================
# PARTE 2: EXTRAÇÃO DE DADOS DO BANCO CENTRAL
# ==========================================
print("Iniciando extração do Banco Central (PTAX)...")
url_bcb = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='01-01-2024'&@dataFinalCotacao='01-31-2024'&$format=json"

response_bcb = requests.get(url_bcb, timeout=30)

if response_bcb.status_code == 200:
    # A API do BCB retorna os dados principais isolados dentro da chave 'value'
    dados_bcb = response_bcb.json()['value']
    df_bcb = pd.DataFrame(dados_bcb)
    
    print("✓ Dados do BCB carregados com sucesso!\n")
    print(df_bcb.head())
    
    # Salvando os dados brutos em CSV no seu diretório customizado
    arquivo_bruto_bcb = OUTDIR / 'bcb_tabela_bruta.csv'
    df_bcb.to_csv(arquivo_bruto_bcb, index=False, encoding='utf-8')
    print(f"\n[Arquivo bruto salvo em: {arquivo_bruto_bcb}]")
    print("-" * 50)
else:
    print(f"Erro ao acessar BCB. Código de status: {response_bcb.status_code}")

# ==========================================
# PARTE 3: TRATAMENTO E VALIDAÇÃO DE DADOS (BCB)
# ==========================================
print("Iniciando tratamento de dados...")

# Criando uma cópia de segurança para tratar os dados do BCB
df_tratado = df_bcb.copy()

# TRATAMENTO 1: Renomear colunas para o padrão "snake_case" (boas práticas)
df_tratado = df_tratado.rename(columns={
    'cotacaoCompra': 'cotacao_compra',
    'cotacaoVenda': 'cotacao_venda',
    'dataHoraCotacao': 'data_hora_cotacao'
})

# TRATAMENTO 2: Converter a coluna de data (string) para o tipo 'datetime' do Pandas
df_tratado['data_hora_cotacao'] = pd.to_datetime(df_tratado['data_hora_cotacao'])

# VALIDAÇÃO DOS DADOS
print("\n--- RESULTADO DA VALIDAÇÃO ---")
print("\n1. Verificação de Tipos e Estrutura (info):")
print(df_tratado.info())

print("\n2. Contagem de Valores Nulos por Coluna:")
print(df_tratado.isnull().sum())

print("\n3. Contagem de Registros Duplicados no Dataset:")
print(df_tratado.duplicated().sum())
print("-" * 50)

# ==========================================
# PARTE 4: EXPORTAÇÃO FINAL
# ==========================================

arquivo_csv_final = OUTDIR / 'dados_tratados.csv'
arquivo_parquet_final = OUTDIR / 'dados_tratados.parquet'

# Salvando em formato CSV (Padrão de mercado para arquivos textuais)
df_tratado.to_csv(arquivo_csv_final, index=False, encoding='utf-8')

# Salvando em formato Parquet (Formato colunar otimizado para Big Data)
df_tratado.to_parquet(arquivo_parquet_final, index=False)

print(f"🚀 PROCESSO CONCLUÍDO! Arquivos processados salvos na pasta '{OUTDIR}':")
print(f" - {arquivo_csv_final.name}")
print(f" - {arquivo_parquet_final.name}")