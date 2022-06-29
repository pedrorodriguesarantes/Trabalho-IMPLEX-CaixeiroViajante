from math import sqrt

def distancia_euclidiana(vertice_A, vertice_B):
    distancia1 = (vertice_A.x - vertice_B.x) * (vertice_A.x - vertice_B.x) 
    distancia2 = (vertice_A.y - vertice_B.y) * (vertice_A.y - vertice_B.y)
    soma = distancia1 + distancia2
    
    return sqrt(soma)
