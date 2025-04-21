#include "register.h"
#include <iostream>
#include <fstream>
using namespace std;

void registerUser() {
    string username, password;
    cout << "Enter username: ";
    cin >> username;
    cout << "Enter password: ";
    cin >> password;
    
    ofstream file("users.txt", ios::app);
    file << username << " " << password << endl;
    file.close();
    
    cout << "Registration successful!" << endl;
}
