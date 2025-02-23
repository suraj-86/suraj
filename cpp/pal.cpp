#include<iostream>
using namespace std;

void palindrome(int a)
{
    int b,original;
    int reversed=0;
    original = a;
    while(a>0){
        b=a%10;
        reversed = reversed*10+b;
        a=a/10;
    }
    if(original==reversed){
        cout<<"this no is palindrome";
    }
    else{
        cout<<"this no is not palindrome";
    }

}

int main()
{
int a;
cout<<"enter the no to check ";
cin>>a;
palindrome(a);
}