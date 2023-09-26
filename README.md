# desafio_pipeline_etl
É o desafio para criar um pipeline de ETL, atividade do Santander Bootcamp 2023 - Ciência de Dados com Python.
O objetivo dessa atividade é criar um pipeline de ETL, onde segue as etapas:
# EXTRACT
Extrair do arquivo Cadastro.csv, as colunas:  UserId, Nome, Cidade e UF

# TRANSFORM
Após a extração, a IA Generativa do Bard é utilizada para assumir o papel de um agente de viagens e sugerir uma viagem no Brasil para um final de semana gastando até R$1.000,00, para cada usuário do arquivo extraído.
Será concatenado os 2 dataframes.

# LOAD
Grava os dados concatenados dos 2 dataframes, o primeiro extraído do arquivo Cadastro.csv, e o segundo são as sugestões de viagens geradas pela IA Generativa do Bard, no arquivo Sugestao_Viagem.csv.
