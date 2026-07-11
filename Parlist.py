# Parlist

'''
    Ovo je Aplikacija za provjeru listi, ideja je da kada se razvije određeni dio ove aplikacije da radi ogromne liste provjera koje 
    bi olakšale posao ljudima i dale bi detaljan feedback na temelju onoga što zasigurno nije u redu sa poslovanjem
    zasada će provjeravati samo potencijalne točke koji nisu pravilno formirani kao razriješeni ciljevi.
'''

# Prvo se uvode sve potrebne biblioteke i moduli koji će se koristiti unutar aplikacije

import sys, numpy as np, pandas as pd, matplotlib.pyplot as plt

# Globalno varijabilna polja i varijable

mjeseci = ["siječanj", "Veljača", "Ožujak", "Travanj", "Svibanj", "Lipanj", "Srpanj", "Kolovoz", "Rujan", "Listopad", "Studeni", "Prosinac"]
prihodi = []
rashodi = []
lose_stanje = False


# Funkcija za napomenu i objašnjenje korištenja aplikacije

def napomena():
    print("-------------------------------------------------------------------------------------------------")
    print("Kako bi se ova aplikacija koristila kako treba potrebno je biti precizan i svaki detalj navesti")
    print("Svaka količina novca se zastupa u valuti eura/EUR")
    print("Korisnik mora prilikom ulaska i početka rada odabrati jednu od funkcionalnosti")
    print("Korisnik će moći analizirati prihod i rashod te provjeriti kako da postigne željeno stanje")
    print("Svaki dio ovog koda je algoritam baziran na matematičkim računicama i kalkulacijama koje detaljno provjeravaju bezbroj mogućih stanja")
    print("")

# Funkcija za izbornik

def izbornik():
    print("1. unos prihoda i rashoda")
    print("2. stanje poslovanja")
    print("3. plan poslovanja")
    print("4. Tablični prikaz")
    print("5. Grafička vizualizacija")
    print("6. izlazak iz sustava")
    print("7. napomena")
    print(" ")
    
# Funkcija za unos mjesečnog prihoda i rashoda

def unos(mjeseci, prihodi, rashodi):
    print("Unesite prihode za svaki mjesec\n-------------------------")
    for i in range(len(mjeseci)):
        x = int(input(f"{i+1}: "))
        prihodi.append(x)
    print("Unesite rashode za svaki mjesec\n-------------------------")
    for i in range(len(mjeseci)):
        y = int(input(f"{i+1}: "))
        rashodi.append(y)
    return prihodi, rashodi

# Funkcija za provjeru stanja nakon izjednačavanja prihoda i rashoda

def provjera_stanja(prihodi, rashodi, lose_stanje):
    if (sum(prihodi) == sum(rashodi)):
        lose_stanje = True
        print("Mi smo na nuli")
        return lose_stanje
    elif (sum(prihodi) < sum(rashodi)):
        lose_stanje = True
        print("U lošem je stanju poslovanje!")
        return lose_stanje
    else:
        lose_stanje = False
        print("U dobrom je stanju poslovanje!")
        return lose_stanje

# Funkcija koja formira stanje na temelju prihoda i rashoda u formatu jedne godine

def stanje(prihodi, rashodi):
    x = sum(prihodi)
    y = sum(rashodi)
    posl_stanje = x - y
    print(f"trenutno stanje jest: {posl_stanje}")
    return posl_stanje

# Funkcija za unos planiranog stanja

def plansko_stanje():
    plan_stanje = int(input("Unesite vaše planirano stanje: "))
    return plan_stanje

# Funkcija za unos plana poslovanja
def plan_poslovanja(prihodi, rashodi, lose_stanje):
    trenutno_stanje = stanje(prihodi, rashodi)
    neostvareno = False
    negativa = False
    plan_stanje = plansko_stanje()
    if trenutno_stanje < plan_stanje:
        neostvareno = True
    if (lose_stanje):
        negativa = True
    if (neostvareno and negativa):
        print("Kako biste ostvarili željeno stanje potrebno je da smanjite rashode!")
        return plan_stanje
    elif (neostvareno and not negativa):
        print( "Kako biste ostvarili željeno stanje potrebno je povečati prihode!")
        return plan_stanje
    elif (not neostvareno and not negativa):
        print("Ostvarili ste već željeno stanje!")
        return  plan_stanje
    else:
        print("Nevažeći unos!")

# Funkcija za tablični zapis prihoda, rashoda i stanja naspram planiranog stanja

def tablicni_zapis(mjeseci, prihodi, rashodi, plan_stanje):
    trenutno_stanje = stanje(prihodi, rashodi)
    df = pd.DataFrame({
        'Mjesec': mjeseci,
        'Prihod': prihodi,
        'Rashod': rashodi
    })
    print(df)
    print(f"\nTrenutno stanje: {trenutno_stanje}\nPlanirano stanje: {plan_stanje}")

# Funkcija za vizualizaciju podataka

def vizualizacija(prihodi, rashodi):
    plt.plot(prihodi, color='b', label='Prihodi')
    plt.plot(rashodi, color='r', label='Rashodi')
    plt.legend()
    plt.show()

# Glavna funkcija koja pokreće cijelu aplikaciju čim je pokrenuta

def main(mjeseci, prihodi, rashodi, lose_stanje, plan_stanje):
    while True:
        napomena()
        while True:
            izbornik()
            odg = int(input("Unesite broj funkcionalnosti (1, 2, 3, 4, 5, 6 ili 7 ): "))
            if odg == 1:
                unos(mjeseci, prihodi, rashodi)
            elif odg == 2:
                provjera_stanja(prihodi, rashodi, lose_stanje)
            elif odg == 3:
                plan_poslovanja(prihodi, rashodi, lose_stanje)
            elif odg == 4:
                tablicni_zapis(mjeseci, prihodi, rashodi, plan_stanje)
            elif odg == 5:
                vizualizacija(prihodi, rashodi)
            elif odg == 6:
                print("U redu, doviđenja!")
                sys.exit()
            elif odg == 7:
                break

main(mjeseci, prihodi, rashodi, lose_stanje, 0)