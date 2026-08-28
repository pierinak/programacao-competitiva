 
def solve_L():
    n, m = map(int, input().split())
    grade = [input().strip() for _ in range(n)]
 
    base = int(grade[0][0])  # cor esperada na posição (0,0)
    valido = True
    for i in range(n):
        linha = grade[i]
        for j in range(m):
            esperado = base ^ ((i + j) % 2)  # alterna a cada passo
            if int(linha[j]) != esperado:
                valido = False
                break
        if not valido:
            break
 
    print("S" if valido else "N")
 