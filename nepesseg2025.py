def main():
    while True:
        keres = fomenu_megjelenites()
        telepulesek = beolvasas()
        if keres == "1":
            megye_adatok(telepulesek)
        elif keres == "2":
            telepules_adatok(telepulesek)
        elif keres == "x":
            break
def fomenu_megjelenites():
    print("")
    print(f"Népesség 2025")
    print(f"Üdvözöllek! Ebben a programban különböző megyék és települések adatait tudod lekérdezni, csak egyszerűen írd be a funkció számát, amit használni szeretnél!")
    print(f"[1] Megye adatai")
    print(f"[2] Település típusai")
    print(f"[3]")
    print(f"[x] Kilépés")
    keres = input(f"Kérem írja ide a funkció jelét amit használni szeretne: ")
    return keres
def beolvasas():
    telepulesek = []
    with open("lakossag_2025.csv", "r", encoding="utf-8") as forras:
        forras.readline()
        for sor in forras:
            adatok = sor.strip().split(";")
            telepules = {
                "megyekod": adatok[0],
                "nev": adatok[1],
                "tipus": adatok[2],
                "ferfi": adatok[3],
                "no": adatok[4],
            }
            ujferf = int(telepules["ferfi"].replace(" ", ""))
            ujno = int(telepules["no"].replace(" ", ""))
            telepules["ferfi"] = ujferf
            telepules["no"] = ujno
            telepulesek.append(telepules)
    return telepulesek
def megye_adatok(telepulesek):
    megye_kod = input(f"Kérem a megye kódját: ").upper()
    tel_szam = 0
    ossz_lak = 0
    varos_lak = 0 
    for tel in telepulesek:
        if tel["megyekod"] == megye_kod:
            tel_szam +=1
            ossz_lak += tel["ferfi"]
            ossz_lak += tel["no"]
        if tel["megyekod"] == megye_kod:
            tel_szam += 1
            ossz_lak += tel["ferfi"] + tel["no"]
            if tel["tipus"] in ["város", "vármegyei jogú város", "vármegye székhely", "fővárosi kerület"]:
                varos_lak += tel["ferfi"] + tel["no"]
    print(f"A {megye_kod} megyében {tel_szam} település található.")
    print(f"A {megye_kod} megyében {ossz_lak} számú lakos él.")
    print(f"A {megye_kod} megyében {varos_lak} számú városi lakos él.")
def telepules_adatok(telepulesek):
    print()
    print(f"Kérem válassza ki milyen típusú települések közt szeretne böngészni.")
    print(f"[a] Városok")
    print(f"[b] Községek")
    inp = input("Írja ide a választása betűjelét: ")
    if inp == "a":
        varosok = []
        for tel in telepulesek:
            if tel["tipus"] == "város" or tel["tipus"] == "vármegyei jogú város" or tel["tipus"] == "vármegye székhely" or tel["tipus"] == "fővárosi kerület":
                nev = tel["nev"]
                lak = tel["ferfi"] + tel["no"]
                varos = {
                    "nev": nev,
                    "lakosok": lak,
                }
                varosok.append(varos)
        lapozas(varosok)
    elif inp == "b":
        varosok = []
        for tel in telepulesek:
            if tel["tipus"] == "nagyközség" or tel["tipus"] == "község":
                nev = tel["nev"]
                lak = tel["ferfi"] + tel["no"]
                kozseg = {
                    "nev": nev,
                    "lakosok": lak,
                }
                varosok.append(kozseg)
        lapozas(varosok)
def lapozas(varosok):
    index = 0
    while index < len(varosok):
        for varos in varosok[index:index + 10]:
            print(f"{varos['nev']} : {varos['lakosok']} fő")
        index += 10
        if index >= len(varosok):
            print("Nincs több megjeleníthető település.")
            break
        print("[1] Folytatom a böngészést")
        print("[2] Inkább nem folytatom a böngészést")
        inp = input("Kérem ide írja a választása számát: ")
        if inp != "1":
            break
main()