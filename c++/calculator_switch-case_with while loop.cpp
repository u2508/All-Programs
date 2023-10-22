#include<stdio.h>
#include<conio.h>
#include<iostream>
using namespace std;
int main()
{
    int a,b,res;
    char opt;
    string choice="yes" ;
    while (choice=="yes" || choice=="1" || choice=="YES" || choice=="Y" || choice=="y")
    {
        printf("enter the operator to be used :- ");
        scanf("%d",&opt);
        printf("enter 1st number :- ");
        scanf("%d",&a);    
        printf("enter 2nd number :- ");
        scanf("%d",&b);
        switch (int(opt))
        {
            //case '+' :
            case 43:
                res=a + b;
                printf("sum of %d and %d is %d",a,b,res);
                break;
            //case '-' :
            case 45:
                res=a - b;
                printf("subtraction of %d and %d is %d",a,b,res);
                break;
            //case '*':
            case 42:
                res=a * b;
                printf("product of %d and %d is %d",a,b,res);
                break;
            //case '/':
            case 47:
                res=a/b;
                printf("on division of %d by %d quotient is %d",a,b,res);
                break;
            //case '%':
            case 37:
                res=a%b;
                printf("on division of %d by %d remainder is %d ",a,b,res);
                break;
            default:
                printf("unknown operation code or name.");
                break;
            
        }

        printf("\nwant to continue :- ");
        cin>> choice;

    }
    exit(printf("Thanks for visiting come again.\nHope you liked it."));
    getch();
}