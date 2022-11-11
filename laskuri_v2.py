#----AlluKoodaa----#

def laskuri():
    litrahinta = input("""
***ALLUN POLTTOAINEKUSTANNUSLASKURI***

Syötä litrahinta tankatessa (€/l):
""").replace(",", ".")
    litrahinta = float(litrahinta)

    kulutus = input("Syötä keskikulutus (l/100km):\n").replace(",", ".")
    kulutus = float(kulutus)

    pituus = float(input("Syötä matkan pituus:\n"))
    kustannus = (pituus / 100) * kulutus * litrahinta
    kyytilaiset = input("Syötä kyytiläisten määrä:\n")

    if kyytilaiset:
        try:
            kyytilaiset = int(kyytilaiset)
        except ValueError:
            print("Tapahtui virhe. Kyytiläisten määrän tulee olla kokonaislukus.")
            exit()
        kustannus = kustannus / (kyytilaiset + 1)
        kustannus = round(kustannus, 2)
        print(f"Matkan polttoainekustannus on {kustannus} euroa per lärvi.")
    else:
        kustannus = round(kustannus, 2)
        print(f"Matkan polttoainekustannus on {kustannus} euroa.")
    print("Kiitos ohjelman käytöstä!")

laskuri()

#----eof----#
