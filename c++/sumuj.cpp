

#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int i ;
    int suma = 0 ;
    int liczba = 0 ;
    int a;
    
    cout <<"Ile liczb chcesz podać: " << endl ;
    cin >> a;
    
    for (i = 0; i < a ; i++)
    {
    
    cout <<"Podaj liczbe : " << endl ;
    cin >> liczba ;
    suma += liczba ;
    //suma = suma + liczba ;
    
    }
    cout << "Suma: " << suma << endl ;
	return 0;
}
