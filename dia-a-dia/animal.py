vertebrado = input().strip()
grupo = input().strip()
alimentacao = input().strip()

if vertebrado == "vertebrado":
    if grupo == "ave":
        if alimentacao == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:  # mamifero
        if alimentacao == "onivoro":
            print("homem")
        else:
            print("vaca")
else:  # invertebrado
    if grupo == "inseto":
        if alimentacao == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:  # anelideo
        if alimentacao == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")