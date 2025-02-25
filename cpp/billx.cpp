//bill for several products

#include<iostream>
using namespace std;

class product{
    public:
        int code;
        string name;
        float price;
        int quantity;
        int total;
    
        void input() {
            cout << "Enter code: ";
            cin >> code;
            cout <<"Enter name: ";
            cin >>name;
            cout << "Enter price: ";
            cin >> price;
            cout << "Enter quantity: ";
            cin >> quantity;
        }
        void bill_print() {            
            total=price*quantity;        
            cout << code <<"   " << name <<"   " << price << "    " << quantity << "    " << total << "\n";
        }
};
    
int main(){
    int a,i;
    cout<<"no of products bought : ";
    cin>>a;

    product item[100];
    float grandTotal = 0;
    for(i=1;i<=a;i++){
        cout<<"\nEnter details of Product "<< i <<"\n";
        item[i].input();
    }
    cout<<"\n\nSURAJ'S SUPER MARKET\n";
    cout<<"-----------------------------";
    cout<< "\nFinal Bill:\n";
    cout<<"-----------------------------\n\n";
    cout<< "Code  Name  Price  Quantity Total\n";
    for(i=1;i<=a;i++){
        item[i].bill_print();
        grandTotal += item[i].total;
    }
    cout<<"\n-----------------------------\n";
    cout << "Grand Total : " << grandTotal << "\n";
}