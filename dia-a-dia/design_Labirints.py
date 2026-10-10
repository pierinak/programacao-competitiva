from collections import deque

def solution():
  t = int(input()) # quantidade de casos de teste
  resultados_teste = [] # armazena os resultados para cada caso de teste
  for teste in range(t):
    no_inicial_n = int(input()) # no inicial

    # duas informações V e A que são respectivamente a quantidade de vértices e arestas do desenho
    linha = input().split()
    qnt_vertices, qnt_arestas = int(linha[0]), int(linha[1])

    #  Uma quantidade A de linhas vem a seguir, cada uma descrevendo um segmento de linha
    vertices = set()
    arestas = set()
    for aresta in range(qnt_arestas):
      linha_arestas = input().split()
      vertice_a, vertice_b = int(linha_arestas[0]), int(linha_arestas[1])
      vertices.add(vertice_a)
      vertices.add(vertice_b)
      arestas.add((vertice_a,vertice_b)) # adiciona uma tupla de origem e destino

    # lista de vizinhos
    vizinhos = {v:[] for v in vertices}
    for origem, destino in arestas:
      vizinhos[origem].append(destino)
      vizinhos[destino].append(origem)

    # percorrendo lista
    qnt_movimentos = -2 
    fronteira = deque([[no_inicial_n]])
    visitados = {no_inicial_n}
    while fronteira:
      path = fronteira.popleft()
      qnt_movimentos += 2 # fiz um movimento

      atual = path[-1]
      if atual == no_inicial_n and len(path) > 1:
        return path

      for vizinho in vizinhos[atual]:
        if vizinho not in visitados:
          visitados.add(vizinho)
          fronteira.append(path+[vizinho])

    
    print(qnt_movimentos)

solution()