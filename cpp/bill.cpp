/*write a program to enter the code and the price of items .
the user must feed the quantity in which he wants a produst .
the program must calculate and display the final bill*/

#include<iostream>
using namespace std;


class product{
    public:
        int code;
        float price;
        int quantity;
    
        void input() {
            cout<< "Details for item \n";
            cout << "Enter code: ";
            cin >> code;
            cout << "Enter price: ";
            cin >> price;
            cout << "Enter quantity: ";
            cin >> quantity;
        }
    
        void bill_print() {                    
            cout<< "Final Bill:\n\n";
            cout<< "Code  Price  Quantity\n";
            cout << code <<"   " << price << "    " << quantity << "\n";
        }
};
    
    
int main(){
    product item;

    item.input();

    float grandTotal = 0;
    item.bill_print();
    grandTotal += item.price * item.quantity;
    cout << "\nGrand Total: " << grandTotal << "\n";
}