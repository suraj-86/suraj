#include <iostream>
using namespace std ;
int fibonacci(int a){
    int next;
    if(a<=1)
        return a;
    next= fibonacci(a-1)+fibonacci(a-2);
    return next;
}
int main(){
    int a;

    cout<<"enter the no of terms to print fibonacci ";
    cin>> a ;
    cout<<"fibonacci series : ";
    int i=0;
    while (i<a){
        cout<<" " <<fibonacci(i);
        i++;
    }
    return 0;
}