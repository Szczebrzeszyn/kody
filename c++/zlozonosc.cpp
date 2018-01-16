

#include <iostream>

using namespace std;

void wypisz_nieparzyste(int x)
{
    for(int i=1;i<=x;i+=2)
    {
        cout<<i<<endl;
    }
}

int main(int argc, char **argv)
{
    int x=0;
    cout<<"Podaj wartosc liczby n:";
    cin>>x;
    
    wypisz_nieparzyste(x);
    
    return 0;
}
