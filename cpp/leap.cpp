#include<iostream>
using namespace std;

void leap(int year){
    if((year%4==0 && year%100!=0)|| (year%400==0)){
        cout<<"LEAP Year";
    }
    else{
        cout<<"Not LEAP Year";
    }
}

int main(){
    int a;
    cout<<"enter year to check : ";
    cin>>a;
    leap(a);

}