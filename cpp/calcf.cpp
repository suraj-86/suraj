#include<iostream>
using namespace std;

void calc(int a,char c,int b){
    switch(c){
        case '+':
            cout<<"result = "<<a+b ;
            break;
        case '-':
            cout<<"result = "<<a-b ;
            break;
        case '*':
            cout<<"result = "<<a*b ;
            break;
        case '/':
            cout<<"result = "<<a/b ;
            break;
        case '%':
            cout<<"result = "<<a%b ;
            break;
        default:
            cout<<"result = "<<"invaled";
            break;
    }
}
int main(){
    int a,b;
    char c;
    cout<<"enter no with operator (like a + b)";
    cin>>a>>c>>b;
    calc(a,c,b);

}