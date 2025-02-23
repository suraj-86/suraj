#include<iostream>
using namespace std;


void swap(int p, int n)
{int temp ;

temp =p ;
p=n;
n=temp;
cout <<"after swap 1st no is "<<p <<" and 2nd no is"<<n;

}

int main()
{
    int a=10,b=20;
    swap(a,b);
    
}