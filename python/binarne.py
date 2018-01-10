#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import floor


def wyszukaj_lin(l, el):
    for i in range(0, len(l)):
        if l[i] == el:
            return i
    return -1


def wyszukaj_bin(lewy, prawy, lista, el):
    lewy, prawy = 0, len(lista) - 1
    while lewy < prawy:
        srodek = floor((lewy + prawy) / 2)
        print(srodek)
        if el <= lista[srodek]:
            prawy = srodek
        else:
            lewy = srodek + 1

    return lewy


def wyszukaj_bin_rek(lewy, prawy, lista, el):
    if lewy > prawy:
        return -1

    srodek = floor((lewy + prawy) / 2)
    if el == lista[srodek]:
        return srodek  # znalezionio element
    if el < lista[srodek]:
        return wyszukaj_bin_rek(lewy, srodek - 1, lista, el)
    else:
        return wyszukaj_bin_rek(srodek + 1, prawy, lista, el)


def sort_wstaw_bin(lista):
    for i in range(1, len(lista)):
        el = lista[i]
        k = wyszukaj_bin(0, i, lista, el)

        lista = lista[:k] + [el] + lista[k:i] + lista[i + 1:]
        print(lista)
    return lista


def main(args):
    lista = [4, 3, 7, 0, 2, 3, 1, 9]
    lista.sort()
    print(lista)
    el = 9
    print(wyszukaj_bin(lista, el))
    print(wyszukaj_bin_rek(0, len(lista) - 1, lista, el))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
