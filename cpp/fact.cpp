#include<iostream>
using namespace std;

int main(){
    int a,b,fact=1;
    
    cout<<"enter no to find factorial ";
    cin>>a;
    for(b=1;b<=a;b++){
        fact*=b;
    }
    cout<<"factorial is "<<fact;
}