#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    masa=float(input("Podaj swoją wagę: "))
    wzrost=float(input("Podaj swój wzrost:"))
    bmi=masa / (wzrost * wzrost)
    if bmi < 18.5:
        print("niedowaga")
    elif bmi < 24.9:
        print("norma")
    elif bmi < 30:
        print("nadwaga")
    elif 30 <= bmi:
        print("otyłość")


    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
