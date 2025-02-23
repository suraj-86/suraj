#include <iostream>
using namespace std;

int fact(int a){
    if(a==0||a==1){
        return 1;
    }
    else{
        return a*fact(a-1);
    }
}


int main() {
    int a;
    cout<<"enter no to check : ";
    cin>>a;
    cout<<"Factorial of "<<a<<" is "<<fact(a);
}