#include <iostream>
using namespace std ;

class sample {
private :
static int count;

public :
void show_count(){
cout<<"\n count = "<<count++;
}
};
int sample::count=1;

int main(){
sample s1,s2,s3,s4;
s1.show_count();
s2.show_count();
s3.show_count();
s4.show_count();
}