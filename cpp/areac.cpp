#include<iostream>
using namespace std;

int area(int a ){
    float ar=a*a*3.14;
        return ar;
}
int main(){
    int r;
    cout<<"enter radius : ";
    cin>>r;
    float ar=area(r);
    cout<<"Area of circle is "<<ar;
}