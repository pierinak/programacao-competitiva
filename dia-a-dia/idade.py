dias = int(input())

anos = dias // 365
resto = dias % 365

meses = resto // 30
dias_restantes = resto % 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias_restantes} dia(s)")