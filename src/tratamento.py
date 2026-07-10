import numpy as np


def tratar_pressao_nula(dataset):
    mediana_pressao = dataset['pressao'].median()
    dataset['pressao'] = dataset['pressao'].fillna(mediana_pressao)
    return dataset


def tratar_temperatura_espuria(dataset):
    mediana_temperatura = dataset[(dataset['temperatura'] != 9999.0) & (dataset['temperatura'].notnull())]['temperatura'].median()
    dataset['temperatura'] = dataset['temperatura'].replace(9999.0, np.nan)
    dataset['temperatura'] = dataset['temperatura'].fillna(mediana_temperatura)
    return dataset


def remover_duplicados(dataset):
    dataset.drop_duplicates(subset=['id'], keep='first', inplace=True)
    return dataset


def tratar_outliers_pressao(dataset, limite=20.0):
    mediana_pressao = dataset['pressao'].median()
    dataset.loc[dataset['pressao'] > limite, 'pressao'] = mediana_pressao
    return dataset
