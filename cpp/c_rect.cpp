#include <iostream>
using namespace std ;

class rectangle {
    private :
        int length,breadth;

    public :
        void get_data(){
            cout<<"enter length and breadth ";
            cin>>length>>breadth;
        }
        void show_data(){
            cout<<"length is "<<length<< " and breadth is "<<breadth<<endl;

        }
        void area(){
            cout<<"Area is "<<length*breadth<<endl;
        }

};
int main(){
    rectangle r1;
    r1.get_data();
    r1.show_data();
    r1.area();
}