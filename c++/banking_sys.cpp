#include <stdlib.h>
#include <iostream>
using namespace std;
extern float p=0.0,r=6.8,t=0.0,pay=0.0;
int loan()
{   pay= (p*r*t/12)/100 +p;
    p=pay;}
int main()
{   int i=0;
    float p1;
    cout<<"enter amount and time in months for loan :- ";
    cin>>p>>t;
    p1=p;
    do {loan();
        i++;}while (i<t);
    cout<<"the total amount to be paid for amount "<<p1<<" is "<<pay;}