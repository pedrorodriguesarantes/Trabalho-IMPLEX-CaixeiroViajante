from funcoes import calcular_distancia, aleatorizar

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

def hillclimbing(vertices, tentativas):
    log_resultados = []

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
        
        caminho = ""
        try:
            for vertice_v in melhor_vertices:
                caminho = caminho + "{}-".format(vertice_v.conteudo)
        except:
            pass
        
        log_resultados.append({
            'MELHOR GLOBAL': melhor_distancia,
            'MELHOR LOCAL': distancia_corrente,
            'CAMINHO': caminho,
        })

        if melhor_distancia == None or melhor_distancia > distancia_corrente:

            melhor_distancia = distancia_corrente
            melhor_vertices = solucao_corrente

        print(melhor_distancia, distancia_corrente)
        
    print(melhor_distancia)
    return melhor_vertices, log_resultados
