# Python para Dados na Prática: 
Consumo de APIs, Boas Práticas e Coleta Ética de Dados 

# o que vamos fazer no módulo

- setup do ambiente (instalar de pendências).

- Consumo de APIs,(ex.: IBGE e Banco Central), Boas Práticas e Coleta Ética de Dados

- Boa práticas e ética na coleta (Revisão da LGPD)

- Atividade Prática: coleta, tratar e salvar dados.

- Resultado esperado: notebook .ipynd + arquivo(s) data/processed/* .csv + README com instruções.

# Entregáveis

- 2 notebook (.ipynb) com documentação explicado cada passo.

- 2 arquivos de dados salvo (CSV e XLSX) dentro da pasta data/Raw.

- 1 README.md curto expricando como rodar o notebook (com comandos pip/conda).


Estrututa do repositório:
Modo 18
|--- README.md
|--- redquirements.txt
|
|--- data/
|  |--- raw/   # Dados brutos baixados (sem tramento)
|  |___ ready  # Dados prontos para análise
|
|___ script/
  |___ python/
    |--- Modo18_bancocentral_api.py
    |___ Modo18_ibge_pop_ webscraping.py







PERGUNTAS:

1) QUAL É MÉDIA DE TRANSAÇÕES VIA PIX POR HABITANTE DE ACORDO COM O MUNCÍPIO BRASILEIRO EM 20257

2) QUAL O MUNICÍPIO BRASILEIRO COM MAIOR NÚMERO DE TRANSAÇÕES VIA PIX EM 20257

3) QUAL O NÚMERO DE TRANSAÇÕES VIA PIX FEITO NO BRASIL EM 2025?
- HIPOTESES:
1 - 55 TRANSAÇÕES POR HABITANTE
2 - SÃO PAULO
3 - 1 BILHÃO

- DADOS NECESSÁRIOS PARA RESPONDER MINHAS PERGUNTAS E HIPOTESES:
¡ - NÚMERO DE TRANSAÇÕES VIA PIX POR MUNICÍPIO BRASILEIRO
ii - NÚMERO DE HABITANTES POR MUNICÍPIO BRASILEIRO

Site:

https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html?edicao=44309

https://dadosabertos.bcb.gov.br/dataset/pix/resource/268e3bf6-b096-4006-83cd-813697012ece