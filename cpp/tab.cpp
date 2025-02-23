#include<iostream>
using namespace std;

void table(int a){
    int i;
    for(i=1;i<=10;i++){
        cout<<a<<"x"<<i<<"="<<a*i<<"\n";
    }
}

int main(){
    int a; 
    cout<<"enter no ";
    cin>>a;
    table(a);
}