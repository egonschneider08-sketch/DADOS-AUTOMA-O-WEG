import os

from carga import carregar_dados, padronizar_colunas
from analise import agrupar_por_status, agrupar_por_genero, resumo_estatistico
from tratamento import tratar_pressao_nula, tratar_temperatura_espuria, remover_duplicados, tratar_outliers_pressao
from graficos import plotar_distribuicao_genero

CAMINHO_CSV = r"C:\Users\matheus_schneider150\Documents\dados_automacao_weg_bruto.csv"

# Carregar dados
dataset = carregar_dados(CAMINHO_CSV)
print("---Primeiras linhas do Database Bruto---")
print(dataset.head())

# Tamanho do dataset
print("--\n Tamanho do Dataset bruto--")
print(dataset.shape)

# Padronizar colunas
dataset = padronizar_colunas(dataset)
print(dataset.head())

# Agrupamentos
print("--- Agrupamento por Status--")
print(agrupar_por_status(dataset))

print("--- Agrupamento por Gênero--")
grupado_genero = agrupar_por_genero(dataset)
print(grupado_genero)

# Gráfico
plotar_distribuicao_genero(grupado_genero)

# Resumo estatístico
print(resumo_estatistico(dataset))

# Valores nulos
print("---Valores NAN por coluna ---")
print(dataset.isnull().sum())
print(f"\nTotal de NAs inicial: {dataset.isna().sum().sum()}")

# Tratamento de pressão
dataset = tratar_pressao_nula(dataset)

# Registros fora do domínio
print("--- Registros Fora do Domínio (Temperatura = 9999) ---")
print(dataset[dataset['temperatura'] == 9999.0])

# Tratamento de temperatura
dataset = tratar_temperatura_espuria(dataset)

# Verificação final de NANs
print("\n --- Verificação Final de NANs por Coluna ---")
print(dataset.isnull().sum())
print(f"Total de NAs atual após tratamentos: {dataset.isna().sum().sum()}")

# Duplicados
duplicados_id = dataset[dataset.duplicated(['id'], keep=False)]
print(f"Total de linhas duplicadas encontradas por ID: {len(duplicados_id)}")
dataset = remover_duplicados(dataset)
print("Duplicados removidos com sucesso!")

# Outliers de pressão
dataset = tratar_outliers_pressao(dataset)

# Dataset final tratado
print("--- DATASET.HEAD() TRATADO ---")
print(dataset.head())

# Exportar
diretorio = "data"
nome_arquivo = "dados_automacao_weg_tratado.csv"
caminho = os.path.join(diretorio, nome_arquivo)
dataset.to_csv(caminho, index=False)
print(f"Dataset tratado salvo em: {caminho}")
