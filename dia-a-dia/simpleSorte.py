a, b, c = map(int, input().split())

original = [a, b, c]
sorted_numbers = sorted(original)

print(*sorted_numbers, sep="\n")
print()
print(*original, sep="\n")