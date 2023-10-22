#include <iostream>
using namespace std;
int main(){
    int a=10;
    try
    {if (a==10)
        {   cout<<"before error\n";
            throw "a";
            cout<<"not to be executed\n";}}
    catch(int )
    {cout<<"error caught error type int";}
    catch (char)
    {cout<<"error caught error type char";}
    catch (const *char)
    {cout<<"error caught error type char";}}