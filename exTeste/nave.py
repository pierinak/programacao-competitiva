n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

valid = True
for i in range(n):
    for j in range(m):
        if j + 1 < m and grid[i][j] == grid[i][j + 1]:
            valid = False
            break
        if i + 1 < n and grid[i][j] == grid[i + 1][j]:
            valid = False
            break
    if not valid:
        break

print("S" if valid else "N")   