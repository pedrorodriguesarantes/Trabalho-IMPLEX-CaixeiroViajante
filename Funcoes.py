from math import sqrt
import numpy as np

def aleatorizar(vertices):
    vertices = vertices.copy()
    vetor = []

    for indice in range(len(vertices)):
        ind = np.random.randint(len(vertices))
        vetor.append(vertices[ind])
        vertices.pop(ind)

    return vetor

def distancia_euclidiana(vertice_A, vertice_B):
    distancia1 = (vertice_A.x - vertice_B.x) * (vertice_A.x - vertice_B.x) 
    distancia2 = (vertice_A.y - vertice_B.y) * (vertice_A.y - vertice_B.y)
    soma = distancia1 + distancia2
    
    return sqrt(soma)

def gera_vizinho(solucao_corrente):
    melhor_solucao = None
    melhor_distancia = None
    y = 0
    while y < len(solucao_corrente):
        x = 0
        while x < y - 1:
            vizinho = solucao_corrente.copy()
            troca = vizinho[x]
            vizinho[x] = vizinho[y]
            vizinho[y] = troca
            distancia_vizinho = calcular_distancia(vizinho)

            if melhor_distancia == None or melhor_distancia > distancia_vizinho:
                melhor_solucao = vizinho.copy()
                melhor_distancia = distancia_vizinho

            x = x + 1
        y = y + 1
    
    return melhor_solucao

def calcular_distancia(vertices):
    distancia = 0

    for indice in range(0, len(vertices) - 1):
        distAB = distancia_euclidiana(vertices[indice], vertices[indice + 1])
        distancia = distancia + distAB

    distancia = distancia + distancia_euclidiana(vertices[indice + 1], vertices[0])
    
    return distancia
