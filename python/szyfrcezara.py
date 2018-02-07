 #!/usr/bin/env python
  # -*- coding: utf-8 -*-
  
 +
  def szyfruj(tekst, klucz):
      """Szyfrowanie tekstu za pomoca szyfru Cezara"""
      klucz = klucz % 26
      szyfrogram = ""
 
 
      for i in tekst:
          ascii = ord(i) + klucz
 -        if ascii > 90:
 +        if ord(i) == 32:
 +            ascii = 32
 +        if ascii > 90 and ascii < 97:
              ascii -= 26
          elif ascii > 122:
              ascii -= 26
 @@ -17,14 +21,25 @@ def szyfruj(tekst, klucz):
  
      return szyfrogram
  
 -def deszyfuj(szyfrogram, klucz):
 +
 +def deszyfruj(szyfrogram, klucz):
      tekst = ""
 -    pass
 +    for i in szyfrogram:
 +        ascii = ord(i) - klucz
 +        if ord(i) == 32:
 +            ascii = 32
 +        if ascii > 90 and ascii < 97:
 +            ascii -= 26
 +        elif ascii > 122:
 +            ascii -= 26
 +        tekst += chr(ascii)
 +
      return tekst
  
  
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
