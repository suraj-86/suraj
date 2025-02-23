#include <iostream>
using namespace std ;
void fibonnacci(int a){
    int i,b=0,c=1,temp;
    for(i=0;i<a;i++){
        cout<<" "<<b;
        temp=b+c;
        b=c;
        c=temp;
    }
}
int main(){
    int a,i;

    cout<<"enter the no of terms to print fibonacci ";
    cin>>a;
    fibonnacci(a);
}