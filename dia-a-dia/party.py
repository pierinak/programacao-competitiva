import sys
import re
from collections import deque

valores = list(map(int, re.findall(r"-?\d+", sys.stdin.read())))
indice = 0
respostas = []

while indice < len(valores):
    n = valores[indice]
    indice += 1

    if n == 0:
        break

    grafo = [[] for _ in range(1001)]

    for _ in range(n):
        x = valores[indice]
        y = valores[indice + 1]
        indice += 2

        grafo[x].append(y)
        grafo[y].append(x)

    visitados = [False] * 1001
    fila = deque([1])
    visitados[1] = True
    total = 0

    while fila:
        pessoa = fila.popleft()
        total += 1

        for vizinho in grafo[pessoa]:
            if not visitados[vizinho]:
                visitados[vizinho] = True
                fila.append(vizinho)

    respostas.append(str(total))

print("\n".join(respostas))