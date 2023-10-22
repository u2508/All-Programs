#include<iostream>
#include<conio.h>
#include<stdio.h>
using namespace std;
int main()
{
    int a,b,res;
    char opt;
    cout<<"enter the operator to be used :- ";
    cin>>opt;
    cout<<"enter 1st number :- ";
    cin>> a;    
    cout<<"enter 2nd number :- ";
    cin>>b;
    if (opt=='+')
    {
        res=a + b;
        cout<<"sum of "<<a<<" and "<<b<<" is "<<res;
    }
    else if (opt=='-')
    {
        res=a - b;
        printf("subtraction of %d and %d is %d",a,b,res);
    }
    else if (opt=='*')
    {
        res=a * b;
        printf("product of %d and %d is %d",a,b,res);
    }
    else if (opt=='/')
    {
        res=a/b;
        printf("on division of %d by %d quotient is %d",a,b,res);
    }
    else if (opt=='%')
    {
        res=a%b;
        printf("on division of %d by %d remainder is %d ",a,b,res);
    }
    else
    {
        printf("operator not found .");
    }
    getch();
    return 0;}