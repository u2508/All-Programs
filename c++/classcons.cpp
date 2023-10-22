#include <iostream>
using namespace std;
class abc
{
public:
    abc();
    ~abc();
};

abc::abc()
{
    cout<<"trash\n";
}

abc::~abc()
{cout<<"program";
}
int main(){
    abc run;
    return 0;
}