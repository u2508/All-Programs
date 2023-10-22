#include<conio.h>
#include<iostream>
using namespace std;
int main()
{
    int i,s,j;
    for ( i = 1; i <= 5; i++)
    {
        for ( s = i; s < 5; s++)
        {
            cout << ' ' ;
        }
        for(j = 1; j <= i; j++)
        {
            cout << "* ";
        }
        cout << '\n';
    }
    getch();
}