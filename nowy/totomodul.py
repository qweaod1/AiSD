import random
import os

def ustawienia():
    """Funkcja pobiera nick użytkownika, ilość losowanych liczb, maksymalną
    losowaną wartość oraz ilość typowań. Ustawienia zapisuje."""

    nick = input("Podaj nick: ")
    nazwapliku = nick + ".ini"
    gracz = czytaj_ust(nazwapliku)
    odp = None
    if gracz:
        print("Twoje ustawienia:\nLiczb: %s\nZ Maks: %s\nLosowań: %s" %
              (gracz[1], gracz[2], gracz[3]))
        odp = input("Zmieniasz (t/n)? ")

    if not gracz or odp.lower() == "t":
        while True:
            try:
                ile = int(input("Podaj ilość typowanych liczb: "))
                maks = int(input("Podaj maksymalną losowaną liczbę: "))
                if ile > maks:
                    print("Błędne dane!")
                    continue
                ilelos = int(input("Ile losowań: "))
                break
            except ValueError:
                print("Błędne dane!")
                continue
        gracz = [nick, str(ile), str(maks), str(ilelos)]
        zapisz_ust(nazwapliku, gracz)

    return gracz[0:1] + [int(x) for x in gracz[1:4]]


def czytaj_ust(nazwapliku):
    if os.path.isfile(nazwapliku):
        plik = open(nazwapliku, "r")
        linia = plik.readline()
        plik.close()
        if linia:
            return linia.split(";")
    return False


def zapisz_ust(nazwapliku, gracz):
    plik = open(nazwapliku, "w")
    plik.write(";".join(gracz))
    plik.close()



def losujliczby(ile, maks):
    liczby = []
    i = 0
    while i < ile:
        liczba = random.randint(1, maks)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i += 1

    return liczby


def pobierztyp(ile, maks):
    typy = set()
    i = 0
    print("Wytypuj %s z %s liczb: " % (ile, maks))
    while i < ile:
        try:
            typ = int(input('Podaj liczbe %s:' % (i+1)))
        except ValueError:
            print('Błędne dane')
            continue

        if 0 < typ < maks and typ not in typy:
            typy.add(typ)
            i += 1

    return typy


def wynik(liczby, typy):
    trafione = liczby & typy
    if trafione:
        print('Trafiłeś %s liczby.' % len(trafione))
        trafione = ', '.join(map(str, trafione))
        print('Trafione liczby: %s' % trafione)
    else:
        print('Nie trafiłeś żadnej liczby. Spróbuj ponownie.')

    return len(trafione)
