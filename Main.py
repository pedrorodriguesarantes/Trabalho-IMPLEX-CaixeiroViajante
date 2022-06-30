from Funcoes import distancia_euclidiana, calcular_distancia, aleatorizar
from HillClimbing import HillClimbing
from SimulatedAnnealing import SimulateAnnealing

import pandas as pd

class Vertice:
    def __init__(self, coordenada_x, coordenada_y, conteudo):
        self.x = float(coordenada_x)
        self.y = float(coordenada_y)
        self.conteudo = conteudo


def importar_vertices(caminho):
    # Montagem da Tabela Virtual no Vetor/Array
    arquivo_lido = None
    
    with open(caminho, 'r') as arquivo:
        arquivo_lido = arquivo.read()
    
    tabela_virtual = []
    arquivo_por_linha = arquivo_lido.split("\n")
    
    for linha in arquivo_por_linha:
        linha_virtual = linha.split()
        tabela_virtual.append(linha_virtual)
        
    if (tabela_virtual[len(tabela_virtual) - 1] == []):
        tabela_virtual.pop()

    dataset = pd.DataFrame(tabela_virtual)
    print(dataset.tail(10))

    vetor_vertices = list()

    for conjunto in dataset.values:
        vertice = Vertice( 
            coordenada_x = conjunto[1], 
            coordenada_y = conjunto[2], 
            conteudo = conjunto[0]
            )

        vetor_vertices.append(vertice)

    return vetor_vertices

def hill(caminho, tentativas):
    vetor_vertices = importar_vertices(caminho = caminho)
    
    solucao = HillClimbing(
        vertices = vetor_vertices, 
        tentativas = tentativas
        )

    return solucao

def siall(caminho):
    vetor_vertices = importar_vertices(caminho = caminho)
    
    solucao, log_resultados = SimulateAnnealing(
            vertices = vetor_vertices, 
            T_max = 10,
            k =  0.95, 
            KT = 20,
            T_min = 5,
        )

    pd.DataFrame(log_resultados).to_csv(
        'Resultados/SimulatedAnnealing - {} - T_MAX {}.csv'.format('att48.tsp.txt', 10), 
        sep = ';'
    )

    return solucao

caminho = 'att48.tsp.txt'
melhor = siall(caminho = 'Exemplos/{}'.format(caminho))