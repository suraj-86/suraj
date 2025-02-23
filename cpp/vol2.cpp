#include<iostream>
using namespace std;

void volume(int len,int width=3,int height=4){
cout<<"length="<<len <<endl;
cout<<"width="<<width <<endl;
cout<<"height="<<height <<endl;

cout<<"volume ="<<len*width*height <<endl <<endl <<endl;
}

int main(){
volume(4,6,2);
volume(4,6);
volume(4);
}