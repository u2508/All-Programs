#include <stdio.h>
#include <string.h>
int main()
{
char n[50],nrev[50];
printf("enter string :- ");
gets(n);
int len=strlen(n)-1;
for (int i = 0; i <= len; i++)
{
    nrev[len-i]=n[i];
}
printf("the reverse of the string %s is %s",n,nrev);
return 0;
}