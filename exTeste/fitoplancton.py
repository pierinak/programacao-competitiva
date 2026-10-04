def solve():
    s = input().strip()
    n = len(s)
    
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    
    # Encontrar o período mínimo
    L = n - pi[n - 1]
    
    if n % L == 0:
        print(n // L)
        print(s[:L])
    else:
        print(1)
        print(s)

solve()   