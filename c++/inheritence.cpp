#include <iostream>
using namespace std;
class a
{public:
    a();
    ~a();};
class b:public a
{private:
    int a1=0,b1=0;
protected:
    int sum;
public:
    int vbb(){
        cin>>a1>>b1;
        sum=a1+b1;
        cout<<sum<<endl;}};
class c :public b
{public :
    int abc(){
        vbb();
        cout<<sum<<endl;
    }};
a::a()
{    cout<<"trash\n";
}
a::~a()
{cout<<"program";
}
int main(){
    c run;
    run.abc();
    return 0;}