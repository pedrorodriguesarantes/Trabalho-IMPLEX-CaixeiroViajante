from Funcoes import calcular_distancia, aleatorizar, gera_vizinho

def HillClimbing(vertices, tentativas):
    melhor_distancia = None
    melhor_vertices = None

    tentativa = 0
    while tentativa < tentativas:
        local = False

        solucao_corrente = aleatorizar(vertices)
        distancia_corrente = calcular_distancia(solucao_corrente)

        while local == False:
            candidato = gera_vizinho(solucao_corrente)
            distancia_candidato = calcular_distancia(candidato)
            
            if distancia_corrente > distancia_candidato:
                distancia_corrente = distancia_candidato
                solucao_corrente = candidato
            else:
                local = True
        
        tentativa = tentativa + 1

        if melhor_distancia == None or melhor_distancia > distancia_corrente:
            melhor_distancia = distancia_corrente
            melhor_vertices = solucao_corrente

        print(melhor_distancia, distancia_corrente)
        
    print(melhor_distancia)
    return melhor_vertices
