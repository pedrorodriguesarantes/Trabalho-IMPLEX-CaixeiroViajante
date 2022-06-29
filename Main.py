from Funcoes import distancia_euclidiana, calcular_distancia, aleatorizar
from HillClimbing import HillClimbing

import pandas as pd

class Vertice:
    def __init__(self, coordenada_x, coordenada_y, conteudo):
        self.x = coordenada_x
        self.y = coordenada_y
        self.conteudo = conteudo


def testar(caminho):
    dataframe = pd.read_csv(caminho, sep=" ", header = None)
    vetorVertices = list()

    for conjunto in dataframe.values:
        vertice = Vertice(conjunto[1], conjunto[2], conjunto[0])
        vetorVertices.append(vertice)

    return vetorVertices

vetorVertices = testar('Exemplos/att48.tsp.txt')
melhor = HillClimbing(vetorVertices, 1000)