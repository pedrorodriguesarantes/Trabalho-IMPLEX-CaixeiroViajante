from Funcoes import distancia_euclidiana, calcular_distancia, aleatorizar
from HillClimbing import HillClimbing

import pandas as pd

class Vertice:
    def __init__(self, coordenada_x, coordenada_y, conteudo):
        self.x = coordenada_x
        self.y = coordenada_y
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

    dataset = pd.read_csv(
        filepath_or_buffer = vetor, 
        sep = " ", 
        header = None
        )

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

caminho = 'att48.tsp.txt'

tentativas = 10
melhor, log_resultados = hill(
    caminho = 'Exemplos/{}'.format(caminho), 
    tentativas = tentativas
    )

pd.DataFrame(log_resultados).to_csv(
    'Resultados/HillClimbing - {} - {}.csv'.format(caminho, tentativas), 
    sep = ';'
    )