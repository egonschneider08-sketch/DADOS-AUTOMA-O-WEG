import matplotlib.pyplot as plt


def plotar_distribuicao_genero(grupado_genero):
    grupado_genero.plot.bar(color='blue')
    plt.title('Distribuição por Gênero do Operador')
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade')
    plt.show()
