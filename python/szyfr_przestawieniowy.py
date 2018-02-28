#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TOBEORNOTTOBETHATISTHEQUESTIONAND


def szyfruj(tekst, klucz):
    szyfrogram = ""
    reszta = len(tekst) % klucz

    if reszta:
        tekst += (klucz - reszta) * "."

<<<<<<< HEAD
    for i in range(klucz): # 0-9
        # print("Wydrukowane i: ", i)
        for j in range(int(len(tekst) / klucz)): # 0-3
=======
    for i in range(klucz):  # 0-9
        # print("Wydrukowane i: ", i)
        for j in range(int(len(tekst) / klucz)):  # 0-3
>>>>>>> 101adda196900f7be6bfceee05ddaf258a63973d
            # print("j: ", j)
            szyfrogram += tekst[i + j * klucz]
    return szyfrogram


def deszyfruj(szyfrogram, klucz):
    tekst = ""
<<<<<<< HEAD
    for i in range(int(len(szyfrogram) / klucz)): # 0-3
        for j in range(klucz): # 0-9
            tekst += szyfrogram[i + (j * int(len(szyfrogram) / klucz))]
            tekst = tekst.replace(".", "")
=======
    for i in range(int(len(szyfrogram) / klucz)):  # 0-3
        for j in range(klucz):  # 0-9
            # print(j)
            # print("i=", i, " + ", "klucz=", int(len(szyfrogram) / klucz), " * ", "j=", j, " rowna sie: ", i + (j * int(len(szyfrogram) / klucz)) )
            tekst += szyfrogram[i + (j * int(len(szyfrogram) / klucz))]
            # tekst = tekst.replace(".", "")
>>>>>>> 101adda196900f7be6bfceee05ddaf258a63973d

    return tekst


def main(args):
    tekst = input("Podaj tekst: ")

    klucz = int(input("Podaj klucz: "))
    # while (2 * klucz > len(tekst)):
    while klucz > (0.5 * len(tekst)):
        klucz = int(input("Podaj klucz: "))

    szyfrogram = szyfruj(tekst, klucz)
    print("Zaszyfrowany: ", szyfrogram)
    deszyfrowany = deszyfruj(szyfrogram, klucz)
    print("Deszyfrowany: ", deszyfrowany)

    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
