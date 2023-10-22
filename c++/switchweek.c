#include <stdio.h>
int main()
{
    int arr;scanf("%d",&arr);
 
    switch (arr)
        {
        case 1 ... 7:
            printf(" WEEK 1 of Month\n");
            break;
        case 8 ... 14:
            printf(" WEEK 2 of Month\n");
            break;
        case 15 ... 21:
            printf(" WEEK 3 of Month\n");
            break;
        case 22 ... 28:
            printf(" WEEK 4 of Month\n");
            break;
        case 29 ... 31:
            printf(" WEEK 5 of Month\n");
            break;
        default:
            printf(" Month has a maximum of 31 days.\n");
            break;
        }

    return 0;
}