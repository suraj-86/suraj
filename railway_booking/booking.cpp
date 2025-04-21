#include <iostream>
#include <fstream>

using namespace std;

#include <iostream>
#include "register.h"  // Include other function declarations
#include "login.h"
#include "schedule.h"
#include "pnr.h"

void bookTicket() {
    string name, train;
    int seat;
    cout << "Enter your name: ";
    cin >> name;
    cout << "Enter train name: ";
    cin >> train;
    cout << "Enter seat number: ";
    cin >> seat;
    
    ofstream file("bookings.txt", ios::app);
    file << name << " " << train << " " << seat << endl;
    file.close();
    
    cout << "Ticket booked successfully!" << endl;
}

int main() {
    std::cout << "Welcome to Railway Booking System\n";
    registerUser();  // Calls function from register.cpp
    loginUser();     // Calls function from login.cpp
    showSchedule();  // Calls function from schedule.cpp
    checkPNR();      // Calls function from pnr.cpp
    return 0;
}