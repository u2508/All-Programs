#include <iostream>
using namespace std;
template<class T>
class ab
{
private:
    T a1=0,b1=0,sum;
public:
    int add(){
        cin>>a1>>b1;
        sum=a1+b1;
        cout<<sum;
        return sum;
    }
};
int main(){
    
    ab <float>a;
    a.add();

    return 0;
}