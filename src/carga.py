import pandas as pd


def carregar_dados(caminho):
    dataset = pd.read_csv(caminho)
    return dataset


def padronizar_colunas(dataset):
    dataset.columns = ['id', 'temperatura', 'pressao', 'status', 'genero', 'consumo_kwh']
    return dataset
