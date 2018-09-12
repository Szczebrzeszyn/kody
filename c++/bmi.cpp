


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	float waga;
    float bmi;
    float wzrost;
    cout <<"Podaj swoją wage : ";
    cin >> waga;
    cout <<"Podaj swój wzrost: ";
    cin >> wzrost;
    bmi=waga/(wzrost*wzrost);
    if (bmi<18.5)
    { 
    cout <<"niedowaga"; 
}
    if (18.5 <= bmi && bmi <24.9)
    {
    cout <<"norma";
}
    if (25 <= bmi && bmi <30)
    {
    cout << "nadwaga";
}
    if (30 < bmi )
    {
    cout <<"Otyłość";    
}

	return 0;
}

