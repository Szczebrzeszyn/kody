/*

 * 
 */


#include <iostream>

using namespace std;
 


int main(int argc, char **argv)
{
    char znak;
    int a,b ;
    a = b = 0 ;
    cout << "Działanie" << endl ;
    cout <<"Podaj liczbe a:" << endl ;
    cin >> a ;
    cout <<"Podaj znak : " <<endl ;
    cin >> znak ;
    cout <<"Podaj liczbe b:" << endl ;
    cin >> b ; 
    if (znak == '+')
    {
     cout << a+b << endl ;
 } 
    if (znak == '-')
    { 
        cout << a-b << endl ; 
    }
    if (znak == '*')
     {
         cout << a*b << endl ; 
     }
    if (znak == '/')
    {
        cout << a/b << endl ;
    }
    
    return 0;
}

