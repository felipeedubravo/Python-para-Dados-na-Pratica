"""
MÓDULO 18: Python e Coleta de Dados
EBAC - Escola Britânica de Artes Criativas e Tecnologia

ETAPAS DO PIPELINE:
2. DOWNLOAD: Baixa o arquivo .xls em modo streaming (por partes) para economizar memória.
3. ARMAZENAMENTO: Salva o arquivo localmente na pasta de dados brutos do projeto.
4. VALIDAÇÃO: Verifica se o download foi concluído com sucesso.

COMO USAR:
1. Instale a dependência executando no terminal:
   pip install requests

2. Execute o script:
   python baixar_xls_original.py

3. O arquivo será salvo em:
   C:/Users/Usuario/Documents/GitHub/Python para Dados na Prática/Mod_18/raw/pop_ibge_2025.xls
   (A pasta é criada automaticamente se não existir)

FONTE DOS DADOS:
IBGE - Estimativas de População 2025
URL: https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html

GLOSSÁRIO:
- FTP: Protocolo de transferência de arquivos (forma de baixar arquivos de servidores).
- Streaming: Download em partes pequenas, evitando sobrecarregar a memória.
- chunk_size: Tamanho de cada parte baixada (8192 bytes ou 8KB por vez).
- Path: Objeto que representa caminhos de arquivos de forma compatível com qualquer sistema operacional.
- raise_for_status(): Verifica se houve erro no download e interrompe a execução se necessário.

OBSERVAÇÕES:
- Este script apenas baixa o arquivo original (.xls).
- Não realiza conversões ou transformações nos dados.
- Se o arquivo já existir, ele será sobrescrito.
- O arquivo baixado será usado como base para processamentos posteriores.
"""

from pathlib import Path
import requests

XLS_URL = "https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2025/POP2025_20260113.xls"

resp = requests.get(XLS_URL, stream=True, timeout=60)
resp.raise_for_status() 

# Diretorio de saida (dados brutos)
OUTDIR = Path(r"C:\Users\Usuario\Documents\GitHub\Python para Dados na Prática\Mod_18\raw") # Define o diretório de saída para salvar os dados brutos obtidos da API.
OUTDIR.mkdir(parents=True, exist_ok=True) # Cria o diretório de saída
XLS_LOCAL = OUTDIR / "pop_ibge_2025.xls"

with open(XLS_LOCAL, "wb") as f:
    for chunk in resp.iter_content(chunk_size=8192):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)      
print("Arquivo salvo em:", XLS_LOCAL)

# finaliza o script
