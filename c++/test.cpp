/* Standard C++ includes */
#include <stdlib.h>
#include <iostream>
#include <conio.h>
using namespace std;
extern int a=0,bc =0;
void loop()
{
    do
    {
        a=a+ ++bc;
        cout<< "case no. "<<bc<<". " << a<<"\n";
    } while (bc<100);
}
int main()
{
    
    int b,c;
    a=b=c=10;
    cout<< a<<"@\n"<<b<<"@\n"<<c<<"@\n"<<bc<<"@\n";
    loop();   
    getch();
    return 0;
}