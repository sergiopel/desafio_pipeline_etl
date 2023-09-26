# O objetivo dessa ETL é extrair dados da planilha Cadastro.csv,
# pegar sugestões na IA generativa e depois carregá-la na planilha Sugestao_Viagem.csv
# No terminal instalar a lib do pandas:
# pip install pandas
############################################################################################### 
# 1 - EXTRACT
# Extrair os campo Id, Nome, Cidade e UF do arquivo Cadasttro.csv para um dataframe do pandas
###############################################################################################
import pandas as pd
df = pd.read_csv('Cadastro.csv')
print(df)

############################################################################################### 
# 2 - TRANSFORM
# Após a extração, a IA Generativa do Bard é utilizada para assumir o papel de um agente de viagens
# e sugerir uma viagem ao Brasil para um final de semana gastando até R$1.000,00,
# para cada usuário do arquivo extraído. Será concatenado os 2 dataframes.
############################################################################################### 
from bardapi import Bard # importa a api do Bard
import os # fornece um conjunto de funções para interagir com o sistema operacional

# Chave da api do Bard, que pode ser obtida pelo browser:
# 1 - botão direito do mouse e selecione inspecionar;
# 2 - selecione a aba Application;
# 3 - na lateral esquerda, em Storage, procure por Cookies e selecione httpd://bard.google.com;
# 4 - procure por "__Secure-1PSID" e copie o Value (que é a chave)
# OBSERVAÇÃO IMPORTANTE, essa chave dá pra usar no programa por volta de 5 vezes, depois disso
# não funcionará mais e será preciso deslogar da conta do google, logar novamente, entrar no
# bard.google.com, atualizar a página e seguir os passos acima novamente
os.environ["_BARD_API_KEY"]="bQhfI9oV4Px0_87rr0kmVvbCuv2qGIXEf9LSg7z7vJPaqd_UuIxwgLqsi9dOjojI3k9GYw."
lista_sug = []

def generate_ai_travels(user, cidade, uf):
  prompt = f"Você é um agente de viagens e quero que sugira para o {user}, que mora em {cidade} - {uf}, uma viagem (100 caracteres) para um final de semana no Brasil gastando até R$1.000,00."
  resposta = Bard().get_answer(str(prompt))['content']
  resposta = resposta.replace("*", "")
  resposta = resposta[: resposta.find("\n")]
  return resposta

for i, row in df.iterrows():
  travel = generate_ai_travels(row[1], row[2], row[3])
  lista_sug.append(travel)

#print()
#print(f"df: {df}")
#print()

df_sug = pd.DataFrame(lista_sug)

#print(f"df_sug: {df_sug}")
#print()

# Combinar os 2 dataframes:
df_novo = pd.concat([df, df_sug], axis=1)
df_novo.columns = ["UserID", "Nome", "Cidade", "UF", "Sugestao"]
#print()
#print(f"df_novo: {df_novo}")

############################################################################################### 
# 3 - LOAD
# Gravar o novo dataframe combinado, no arquivo "Sugestao_Viagens.csv"
df_novo.to_csv("Sugestao_Viagens.csv", header=True, index_label=False)
############################################################################################### 