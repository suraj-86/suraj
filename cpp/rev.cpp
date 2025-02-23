#include<iostream>
using namespace std;

void reversed(int a){
    int reversed,b;
    while(a>0){
        b=a%10;
        a=a/10;
        reversed=reversed*10+b;
        //cout<<b;
    }
    cout<<"final reversed no is "<<reversed;
}

int main()
{
    int a;
    cout<<"enter the no ";
    cin>>a;
    reversed(a);
}