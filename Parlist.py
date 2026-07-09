# Parlist

'''
    Ovo je Aplikacija za provjeru listi, ideja je da kada se razvije određeni dio ove aplikacije da radi ogromne liste provjera koje 
    bi olakšale posao ljudima i dale bi detaljan feedback na temelju onoga što zasigurno nije u redu sa poslovanjem
    zasada će provjeravati samo potencijalne točke koji nisu pravilno formirani kao razriješeni ciljevi.
'''

# Prvo se uvode sve potrebne biblioteke i moduli koji će se koristiti unutar aplikacije

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
    print("1. prihod")
    print("2. rashod")
    print("3. stanje poslovanja")
    print("4. plan poslovanja")
    print("5. izlazak iz sustava")
    
# Funkcija za unos mjesečnog prihoda i rashoda

def unos(mjeseci, prihodi, rashodi):
    print("Unesite prihode za svaki mjesec\n-------------------------")
    for i in range(len(mjeseci)):
        x = int(input(f"{i}: "))
        prihodi.append(x)
    print("Unesite rashode za svaki mjesec\n-------------------------")
    for i in range(len(mjeseci)):
        y = int(input(f"{i}: "))
        rashodi.append(x)
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

# Glavna funkcija koja pokreće cijelu aplikaciju čim je pokrenuta

def main(mjeseci, prihodi, rashodi, lose_stanje):
    napomena()
    unos(mjeseci, prihodi, rashodi)
    provjera_stanja(prihodi, rashodi, lose_stanje)
main(mjeseci, prihodi, rashodi, lose_stanje)