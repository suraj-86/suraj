#include<iostream>
using namespace std;

int main()
{
    int a,b,fact=1;
    
    cout<<"enter no to check ";
    cin>>a;
    if(a%2==0 or a%3==0 or a%5==0 or a%7==0){
        cout << "Composite no";
    }
    else{
        cout <<"Prime no";
    }
}