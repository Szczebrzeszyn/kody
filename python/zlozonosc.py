#!/usr/bin/env python
# -*- coding: utf-8 -*-


def wypisz_nieparzyste(y):
    for i in range(1, y, 2):
        print(i)


def main(args):
    y = int(input(" Podaj wartosc liczby n: "))

    wypisz_nieparzyste(y)

    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
