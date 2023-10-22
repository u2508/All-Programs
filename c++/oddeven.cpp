#include <iostream>
using namespace std;
class ab
{
private:
    int a;
public:
    int c(){
        if (a%2==0)
        {
            cout<<"f u";
        }

    }
    ab(){
        cin>>a;
    }
};
int main(){
    ab a;
    a.c();
}