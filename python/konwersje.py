#!/usr/bin/env python
# -*- coding: utf-8 -*-


def dec2other(liczba10, podstawa):
    """Konwersja liczby dziesiętnej na system o podanej podstawie"""
    liczba = []  # pusta lista dla zapamiętywania reszt
    while liczba10 != 0:
        reszta = liczba10 % podstawa
        if reszta > 9:  # wykorzystanie kodu ASCII
            reszta = chr(reszta + 55)  # obliczanie reszt z dzielenia
        liczba.append(str(reszta))
        liczba10 = int(liczba10 / podstawa)
    liczba.reverse()  # odwracanie
    return "".join(liczba)  # uwaga


def zamiana1():
    """Pobieranie danych wejściowych"""
    liczba = int(input("Podaj liczbę :"))
    podstawa = int(input("Podaj podstawe :"))
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawe:"))
    print("Wynik konwersji : {}(10) = {}({})".format(
        liczba, dec2other(liczba, podstawa), podstawa))


def other2dec(liczba, podstawa):
    """Zamiana podanej liczby na dziesiętnej"""
    # 123(7) = 1*7^2 + 2*7^1 + 3*7^0
    liczba = 0
    potega = len(liczba) - 1
    for cyfra in liczba:
        liczba10 += int(cyfra) *(podstawa**potega)
        potega -=1

def zamiana2():
    """Pobieranie danych wejściowych"""
    liczba = input("Podaj liczbę :")  # ABC
    podstawa = int(input("Podaj podstawe :"))
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawe:"))
    print("Wynik konwersji : {}({}) = {}(10)".format(
        liczba, podstawa, other2dec(liczba, podstawa)))


def main(args):
    print("Zamiana liczby dziesiętnej na liczbę o podanej podstawie ""<2;16>lub odwrotnie")
    zamiana1()
    zamiana2()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
