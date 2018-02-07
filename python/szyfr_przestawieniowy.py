#!/usr/bin/env python
# -*- coding: utf-8 -*-



def szyfruj(tekst, klucz)
    reszta  =len(tekst) % klucz
    if reszta:
        tekst += (klucz - reszta) * "."
        print(tekst)


def main(args):
    tekst = input("Podaj tekst: ")
    klucz = int(input("Podaj klucz: "))
    szyfrogram = szyfruj(tekst, klucz)
    print(szyfrogram)
    # print(deszyfruj(szyfrogram, klucz))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
