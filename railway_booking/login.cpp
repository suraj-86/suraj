#include "login.h"
#include <iostream>
#include <fstream>
using namespace std;

bool loginUser() {
    string username, password, u, p;
    cout << "Enter username: ";
    cin >> username;
    cout << "Enter password: ";
    cin >> password;
    
    ifstream file("users.txt");
    while (file >> u >> p) {
        if (u == username && p == password) {
            return true;
        }
    }
    return false;
}