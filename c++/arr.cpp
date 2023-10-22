#include <stdio.h>
#include <string.h>
int main()
{   char n[50];
    gets(n);
    for (int i = 0; i < strlen(n); i++)
    {printf("%c ",n[i]);} }    
