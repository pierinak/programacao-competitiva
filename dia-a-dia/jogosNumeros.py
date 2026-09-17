from collections import deque

def menor_operacoes(X, Y, A):
    if X == Y:
        return 0

    MAXV = 100000
    dist = [-1] * (MAXV + 1)
    fila = deque([X])
    dist[X] = 0

    while fila:
        v = fila.popleft()

        for ai in A:
            ops = [
                v + ai,
                v - ai,
                v * ai
            ]

            if v % ai == 0:
                ops.append(v // ai)

            for nxt in ops:
                if 1 <= nxt <= MAXV and dist[nxt] == -1:
                    dist[nxt] = dist[v] + 1
                    if nxt == Y:
                        return dist[nxt]
                    fila.append(nxt)

    return -1