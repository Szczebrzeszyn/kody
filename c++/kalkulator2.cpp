

#include <iostream>
using namespace std;

int sumuj(int a, int b)

{
    int wynik = a+b;
    return wynik;
}

int odejmij(int a, int b)

{    
    int wynik = a- b;
    return wynik;
}

int mnozenie(int a, int b)

{
    int wynik = a*b;
    return wynik;
}

int dzielenie(int a, int b)

{
    float wynik = a/b ;
    return wynik;
}

int main(int argc, char **argv)
{
	int a, b;
    a = b = 0 ;
    cout << " Pierwsza liczba :";
    cin >> a ;
    cout << " Druga liczba :" ;
    cin >> b;
    cout << "Suma : " << sumuj(a, b) ;
    cout << "Różnica : " << odejmij(a,b);
    cout << "Iloczyn : " << mnozenie(a, b);
    cout << "Iloraz : " << dzielenie(a, b);
    
	return 0;
}

