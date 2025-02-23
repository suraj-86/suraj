#include<iostream>
using namespace std;

int main()
{
    int a,b,c,d,e;
    cout << "enter principle : ";
    cin >>a;
    cout << "enter rate : ";
    cin >>b;
    cout << "enter time : ";
    cin >>c;
    d=(a*b*c)/100;
    e=a+d;
    cout << "simple interest is : " <<d;
    cout<< " total sum is " << e;
    
}