import glob
import os

#1
def leia_projektifailid(tip):
    failid = glob.glob(f"*{tip}")
    return failid

#2
def analuusi_faili_sisu(fail):
    read_lines = 0
    empty_lines = 0
    fixme_todo = 0
    with open(fail, "r", encoding="utf-8", errors="ignore") as f:
        for rida in f:
            read_lines += 1
            if rida.strip() == "":
                empty_lines += 1
            fixme_todo += rida.count("TODO") + rida.count("FIXME")
    return {"fail": fail, "read_lines": read_lines, "empty_lines": empty_lines, "TODO/FIXME": fixme_todo}

#3
def loo_raporti_kataloog(nimi="Analüüsi_Raportid"):
    if not os.path.exists(nimi):
        os.mkdir(nimi)
    return nimi

#4
def leia_failid_algustahega(taht):
    return glob.glob(f"{taht}*.*")



raport = []

loo_raporti_kataloog()

while True:
    print(f"""\nTere tulemast mega analüüsatoris 3000
    Vali tegevus.
    1. Teosta täisanalüüs.
    2. Salvesta raport faili.
    3. Puhasta logid.
    4. Otsi faili algustähe järgi.
    0. Välju
    """)
    try:
        vali = int(input())
    except ValueError:
        print("Kirjuta ainult arv.")

    if vali == 1:
        tip = input("Sisesta fail tüüp (.py, .txt, .java): ")
        failid = leia_projektifailid(tip)

        if not failid:
            print("Ei leitud ühtegi faili.")
            continue
        else:
            for fail in failid:
                tulemused = analuusi_faili_sisu(fail)
                print(tulemused)
                raport.append(tulemused)
                continue

    elif vali == 2:
        if not raport:
            print("Raport on tühi. Teosta analüüs enne salvestamist.")
            continue
        kataloog = loo_raporti_kataloog()
        raport_faili_nimi = os.path.join(kataloog, "analüüsi_raport.txt")
        with open(raport_faili_nimi, "w", encoding="utf-8") as rf:
            for kirje in raport:
                rf.write(f"{kirje}\n")
        print(f"Raport salvestatud faili: {raport_faili_nimi}")
        continue

    elif vali == 3:
        kataloog = "Analüüsi_Raportid"
        for f in os.listdir(kataloog):
            os.remove(os.path.join(kataloog, f))
        os.rmdir(kataloog)
        print("Logid on puhastatud.")
        loo_raporti_kataloog()
        raport = []
        continue

    elif vali == 4:
        taht = input("Sisesta taht: ")
        algustaht = leia_failid_algustahega(taht)
        print(algustaht)
        raport.append(algustaht)
        continue
    elif vali == 0:
        print("Head aega!")
        break

