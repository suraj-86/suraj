#include<iostream>
using namespace std;

int volume(int len,int width=3,int height=4){
    int vol;
    cout<<"length="<<len <<endl;
    cout<<"width="<<width <<endl;
    cout<<"height="<<height <<endl;
    //cout<<"volume ="<<len*width*height <<endl <<endl <<endl;
    vol=len*width*height;
    return vol;
}

int main(){
    int a,b,c;
        
    a=volume(4,6,2);
    cout<<"volume is " <<a <<endl;
    b=volume(4,6);
    cout<<"volume is " <<b<<endl;
    c=volume(4);
    cout<<"volume is " <<c<<endl;
}