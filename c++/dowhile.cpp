#include<conio.h>
#include<iostream>
using namespace std;
int main()
{
    int b=15 ,count=0;
    do
    {
        int a=15;
        a-=count;
        do
        {
            cout<< '*';
            a-=1;
        } while (a>10);
        cout<< '\n';
        count+=1;
        b-=1;
    } while (b>10);
    getch();
}