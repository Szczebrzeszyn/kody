#!/usr/bin/env python
# -*- coding: utf-8 -*-

<<<<<<< HEAD
def szyfruj(tekst, haslo):
    litery = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tablica = [(litery * 2)[i:i+26] for i in range(26)]
    print('\n'.join(tablica))
=======

def szyfruj(tekst, haslo):
    szyfrogram = []
    # litery = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSTUVWXYZŹŻ'
    litery = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    litera_hasla = 0

    for i in tekst:
        index = litery.find(i)  # szuka w liscie litery indexu 'i' z tekstu
        # print("Numer: ", num)
        if index != -1:  # jesli litera z tekstu nie znalazla sie w alfabecie
            index += litery.find(haslo[litera_hasla])
            # jesli wyjdziemy poza 26(litery alfabetu) to dzielimy modulo przez 26 i dodajemy reszte
            index %= 26
            # index %= 34 # dla alfabetu polskiego

            szyfrogram.append(litery[index])
            litera_hasla += 1  # przechodzimy do kolejnej litery w hasle
            if litera_hasla == len(haslo):
                litera_hasla = 0
        else:
            szyfrogram.append(i)

    return "".join(szyfrogram)


def deszyfruj(szyfrogram, haslo):
    tekst = []
    # litery = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSTUVWXYZŹŻ'
    litery = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    litera_hasla = 0

    for i in szyfrogram:
        index = litery.find(i)
        if index != -1:
            index -= litery.find(haslo[litera_hasla])
            index %= 26
            # index %= 34 # dla alfabetu polskiego

            tekst.append(litery[index])
            litera_hasla += 1
            if litera_hasla == len(haslo):
                litera_hasla = 0
        else:
            tekst.append(i)

    return "".join(tekst)

>>>>>>> 101adda196900f7be6bfceee05ddaf258a63973d

def main(args):
    tekst = input("Podaj tekst: ")
    haslo = input("Podaj hasło: ")
<<<<<<< HEAD

    szyfrogram = szyfruj(tekst.upper(), haslo.upper())

    print(szyfrogram)
    print(deszyfruj(szyfrogram, haslo))
    return 0


=======
    tekst = tekst.upper()
    haslo = haslo.upper()

    szyfrogram = szyfruj(tekst, haslo)

    print("Zaszyfrowane: ", szyfrogram)
    print("Deszyfrowane: ", deszyfruj(szyfrogram, haslo))

    return 0
# =ZNAK(JEŻELI(WIERSZ(A1)+KOLUMNA(A1)+63>90;WIERSZ(A1)+KOLUMNA(A1)+63-26;WIERSZ(A1)+KOLUMNA(A1)+63))
>>>>>>> 101adda196900f7be6bfceee05ddaf258a63973d


if __name__ == '__main__':
    import sys
<<<<<<< HEAD
sys.exit(main(sys.argv))
=======
    sys.exit(main(sys.argv))
>>>>>>> 101adda196900f7be6bfceee05ddaf258a63973d
