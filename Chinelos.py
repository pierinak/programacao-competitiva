N = int(input())
estoque = [int(input()) for _ in range(N)]

P = int(input())
vendidos = 0

for _ in range(P):
    tamanho = int(input())
    if estoque[tamanho - 1] > 0:
        estoque[tamanho - 1] -= 1
        vendidos += 1

print(vendidos)     