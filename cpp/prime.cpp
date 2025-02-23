#include<iostream>
using namespace std;

int main()
{
    int a,i;
    bool count=true;
    
    cout<<"enter no to check ";
    cin>>a;
    if(a<2){
        cout << "Neither prime nor composite " << endl;
        return 0;
    }
    for(i=2;i<a;i++){
        if(a%i==0){
            count= false;
            break;
        }
    }
    if(count){
        cout << "Prime no" << endl;
    }
    
    else{
        cout << "Composite no" << endl;
    }
}