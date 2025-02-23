#include <iostream>
using namespace std ;
int main(){
    int a,i;
    int b=0,c=1,temp;

    cout<<"enter the no of terms to print fibonacci ";
    cin>>a;
    for(i=0;i<a;i++){
        cout<<" "<<b;
        temp=b+c;
        b=c;
        c=temp;
    }
}