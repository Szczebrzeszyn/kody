#include <iostream>
#include <cstdlib>
 
using namespace std;
 
int silnia (int liczba)
{
    if (liczba<2) return liczba;
    return liczba*silnia(liczba-1);
}
 
 
 int silnia_rek(int n)
{
	if (n < 2)
		return 1;
	return n * silnia_rek(n - 1) ;
}
 
 
int main()
{
    int s;
 
    cout << "podaj liczbe" << endl;
    cin >> s;
 
    cout << "silnia: "<< silnia_rek(s) << endl;
    return 0;
}
