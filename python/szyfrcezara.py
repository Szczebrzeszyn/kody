#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj(tekst, klucz):

    szyfrogram = ""
    klucz = klucz % 26

    for znak in tekst:
        ascii = ord(znak) + klucz
        if ascii > 90:
            ascii -= 26
        szyfrogram += chr(ascii)
    return szyfrogram


def main(args):
    tekst = input("podaj tekst:")
    klucz = int(input("Podaj klucz:"))
    szyfrogram = szyfruj(tekst, klucz)
    print(szyfrogram)
    print(deszyfruj(szyfrogram, klucz))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
