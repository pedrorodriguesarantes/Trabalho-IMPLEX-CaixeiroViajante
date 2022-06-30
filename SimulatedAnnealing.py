from Funcoes import aleatorizar, calcular_distancia
import numpy as np

def gerar_vizinho(solucao_corrente):
    solucoes = []

    y = 0
    while y < len(solucao_corrente):
        x = 0
        while x < y - 1:
            vizinho = solucao_corrente.copy()
            
            troca = vizinho[x]
            vizinho[x] = vizinho[y]
            vizinho[y] = troca

            solucoes.append(vizinho.copy())
            x = x + 1
        y = y + 1
    
    aleatorio = np.random.randint(0, len(solucoes))
    return solucoes[aleatorio]

def SimulateAnnealing(vertices, T_max, k, KT, T_min):
    T = T_max
    melhor_solucao = aleatorizar(vertices)
    melhor_distancia = calcular_distancia(melhor_solucao)

    while T < T_min:
        t = 0
        
        while t != KT:
            vizinho = gerar_vizinho(solucao_corrente)
            distancia_vizinho = calcular_distancia(vizinho)
            
            if distancia_vizinho < melhor_distancia:
                melhor_distancia = distancia_vizinho
                melhor_solucao = vizinho
            
            else:
                sub = melhor_distancia - distancia_vizinho
                verificar = 2.71828 ^ ((sub) / T)
                
                if np.random.randint(0, 1) < verificar:
                    melhor_solucao = vizinho
                    melhor_distancia = distancia_vizinho

            t = t + 1
        T = k * T
    return