#include<iostream>
using namespace std;

int power(int base , int exp ){
    int result=1,i;
    for(i=0;i<exp;i++){
        result*=base;
    }
        return result;
}

int main(){
    int a,b;
    cout<<"Enter base and exponent (with space in between) : ";
    cin>>a>>b;
    cout<<a<<" to the power of "<<b<<" = "<<power(a,b);

}