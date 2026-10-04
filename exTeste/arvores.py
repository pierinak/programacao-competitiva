import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n = int(input())
    
    adj = [[] for _ in range(n + 1)]
    for idx in range(1, n + 1):
        u, v = map(int, input().split())
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    
    visited = [False] * (n + 1)
    answer = -1
    
    def dfs(u, parent):
        nonlocal answer
        visited[u] = True
        for v, edge_id in adj[u]:
            if v == parent:
                continue
            if visited[v]:
                # Aresta que fecha o ciclo!
                answer = edge_id
                return True
            if dfs(v, u):
                return True
        return False
    
    dfs(1, 0)
    print(answer)

solve()   