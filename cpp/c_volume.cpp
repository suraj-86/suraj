#include <iostream>
using namespace std ;

int volume(int side){
    return side*side*side;
}
float volume(float radius , float height){
    return 3.14*radius*radius*height;
}
long int volume (int length,int breadth,int height){
    return length*breadth*height;
}

int main(){
    int s,l,b,height;
    float r,h;
    cout<<"enter side of cube ";
    cin>>s;
    cout<<volume(s)<<endl;
    
    cout<<"enter radius and height ";
    cin>>r>>h;
    cout<<volume(r,h)<<endl;

    cout<<"enter length breadth and height ";
    cin>>l>>b>>height;
    cout<<volume(l,b,height)<<endl;
}