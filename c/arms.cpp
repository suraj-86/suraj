#include<iostream>
using namespace std;

int power(int a , int b ){
    int result=1,i;
    for(i=0;i<b;i++){
        result*=a;
    }
        return result;
}

void armstrong(int a,int n){
    int original=a,b,c=0;
    while(a!=0){
        b=a%10;
        c=c+power(b,n);
        a/=10;
    }
    if(c==original){
        cout << "this is armstrong no" << endl;
    }
    else {
        cout << "this no is not armstrong" << endl;
    }
}

int main(){
    int a,b;
    cout<<"enter no to check ";
    cin >> a;
    cout<<"enter no of digits ";
    cin >> b;
    armstrong(a,b);
}