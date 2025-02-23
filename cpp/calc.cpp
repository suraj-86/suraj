#include<iostream>
using namespace std;

int main(){
    int a,b;
    char c;
    cout<<"enter no with operator (like a + b)";
    cin>>a>>c>>b;

    switch(c){
        case '+':
            cout<<a+b ;
            break;
        case '-':
            cout<<a-b ;
            break;
        case '*':
            cout<<a*b ;
            break;
        case '/':
            cout<<a/b ;
            break;
        case '%':
            cout<<a%b ;
            break;
        default:
            cout<<"invaled";
            break;
    }
    return 0;
}