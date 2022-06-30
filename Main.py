from funcoes import distancia_euclidiana, calcular_distancia, aleatorizar
from hillclimbing import hillclimbing
from simulatedannealing import simulatedannealing

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
    
    solucao = hillclimbing(
        vertices = vetor_vertices, 
        tentativas = tentativas
        )

    return solucao

def siall(caminho, t_max, k, kt, t_min):
    vetor_vertices = importar_vertices(caminho = caminho)
    
    solucao, log_resultados = simulatedannealing(
            vertices = vetor_vertices, 
            T_max = t_max,
            k =  k, 
            KT = kt,
            T_min = t_min,
        )

    pd.DataFrame(log_resultados).to_csv(
        'Resultados/SimulatedAnnealing - {} - T_MAX {}.csv'.format('att48.tsp.txt', t_max), 
        sep = ';'
    )

    return solucao

caminho = 'att48.tsp.txt'
melhor = siall(
    caminho = 'Exemplos/{}'.format(caminho),
    t_max = 10,
    k = 0.95,
    kt = 20,
    t_min = 5
    )

melhor = siall(
    caminho = 'Exemplos/{}'.format(caminho),
    t_max = 100,
    k = 0.9,
    kt = 25,
    t_min = 10
    )