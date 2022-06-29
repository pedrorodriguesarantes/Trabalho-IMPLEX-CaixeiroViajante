from Distancia import distancia_euclidiana

class Vertice:
    def __init__(self, coordenada_x, coordenada_y, conteudo):
        self.x = coordenada_x
        self.y = coordenada_y
        self.conteudo = conteudo

class Aresta:
    def __init__(self, vertice_A, vertice_B):
        self.A = vertice_A
        self.B = vertice_B
        self.distancia = distancia_euclidiana(vertice_A, vertice_B)