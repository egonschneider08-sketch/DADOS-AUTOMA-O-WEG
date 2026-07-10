def agrupar_por_status(dataset):
    return dataset.groupby(['status']).size()


def agrupar_por_genero(dataset):
    return dataset.groupby(['genero']).size()


def resumo_estatistico(dataset):
    return dataset.describe()
