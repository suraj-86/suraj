#include "pnr.h"
#include <iostream>
#include <fstream>
using namespace std;

void checkPNR() {
    string name, train, searchName;
    int seat;
    bool found = false;

    cout << "Enter your name to check PNR status: ";
    cin >> searchName;

    ifstream file("database/bookings.txt");
    
    while (file >> name >> train >> seat) {
        if (name == searchName) {
            cout << "PNR Status: Confirmed | Train: " << train << " | Seat No: " << seat << endl;
            found = true;
            break;
        }
    }

    if (!found) {
        cout << "No booking found for the entered name!" << endl;
    }

    file.close();
}
