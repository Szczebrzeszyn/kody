#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj(tekst, klucz):
    """Szyfrowanie tekstu za pomoca szyfru Cezara"""
    klucz = klucz % 26
    szyfrogram = ""
    # znaki_pl = ["Ą", "Ć", "Ę", "Ł", "Ń", "Ó", "Ś", "Ź", "Ż", "ą", "ć", "ę",
    #         "ł", "ń", "ó", "ś", "ź", "ż"]
    for i in tekst:
        ascii = ord(i) + klucz
        if ord(i) == 32:
            ascii = 32
        if ascii > 90 and ascii < 97:
            ascii -= 26
        elif ascii > 122:
            ascii -= 26

        szyfrogram += chr(ascii)

    return szyfrogram


def deszyfruj(szyfrogram, klucz):
    tekst = ""
    for i in szyfrogram:
        ascii = ord(i) - klucz
        if ord(i) == 32:
            ascii = 32
        if ascii > 90 and ascii < 97:
            ascii -= 26
        elif ascii > 122:
            ascii -= 26
        tekst += chr(ascii)

    return tekst

# oblsłuzyć male i duże litery
# obsluzyc spacje


def main(args):
    tekst = input("Podaj tekst: ")
    klucz = int(input("Podaj klucz: "))
    szyfrogram = szyfruj(tekst, klucz)

    print(szyfrogram)
    print(deszyfruj(szyfrogram, klucz))

    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
