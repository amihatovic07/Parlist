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
    print("4. izlazak iz sustava")
    print("5. napomena")
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
        return "Mi smo na nuli", lose_stanje
    elif (sum(prihodi) < sum(rashodi)):
        lose_stanje = True
        return "U lošem je stanju poslovanje!", lose_stanje
    else:
        lose_stanje = False
        return "U dobrom je stanju poslovanje!", lose_stanje

# Funkcija koja formira stanje na temelju prihoda i rashoda u formatu jedne godine

def stanje(prihodi, rashodi):
    x = sum(prihodi)
    y = sum(rashodi)
    stanje = x - y
    return stanje

# Funkcija za unos plana poslovanja

def plan_poslovanja(prihodi, rashodi, lose_stanje):
    trenutno_stanje = stanje(prihodi, rashodi)
    neostvareno = False
    negativa = False
    plan_stanje = int(input("Unesite vaše planirano stanje: "))
    if trenutno_stanje < plan_stanje:
        neostvareno = True
    if (lose_stanje):
        negativa = True
    if (neostvareno and negativa):
        return "Kako biste ostvarili željeno stanje potrebno je da smanjite rashode!"
    elif (neostvareno and not negativa):
        return "Kako biste ostvarili željeno stanje potrebno je povečati prihode!"
    elif (not neostvareno and not negativa):
        return "Ostvarili ste već željeno stanje!"
    else:
        return "Nevažeći unos!"



# Glavna funkcija koja pokreće cijelu aplikaciju čim je pokrenuta

def main(mjeseci, prihodi, rashodi, lose_stanje):
    while True:
        napomena()
        while True:
            izbornik()
            odg = int(input("Unesite broj funkcionalnosti (1, 2, 3, 4 ili 5): "))
            if odg == 1:
                unos(mjeseci, prihodi, rashodi)
            elif odg == 2:
                provjera_stanja(prihodi, rashodi, lose_stanje)
            elif odg == 3:
                plan_poslovanja(stanje(prihodi, rashodi), provjera_stanja(prihodi, rashodi, lose_stanje))
            elif odg == 4:
                sys.exit()
            elif odg == 5:
                break

main(mjeseci, prihodi, rashodi, lose_stanje)