#!/usr/bin/env python
# -*- coding: utf-8 -*-


def euklides(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


def euklides2(a, b):
    while a > 0:

            a= a % b
            b = b - a

    return b

def main(args):

    a = int(input("podaj liczbe:"))
    b = int(input("podaj liczbe:"))
    assert euklides2(10, 5) == 5
    print("nwd {:d} ,{:d} = {:d}".format(a, b, euklides(a, b)))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
