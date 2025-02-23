#include <iostream>
using namespace std ;

void eo(int a){
    if(a%2==0){
        cout<<"EVEN";
    }
    else{
        cout<<"ODD";
    }
}
int main(){
    int a;
    cout<<"enter no to check : ";
    cin>>a;
    eo(a);

}