#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Passenger {
    string name;
    int age;
    string source;
    string destination;

public:
    Passenger(string n, int a, string s, string d) {
        name = n;
        age = a;
        source = s;
        destination = d;
    }

    void displayPassenger() {
        cout << "Name       : " << name << endl;
        cout << "Age        : " << age << endl;
        cout << "From       : " << source << endl;
        cout << "To         : " << destination << endl;
        cout << "-----------------------------" << endl;
    }
};

class Train {
    int trainNumber;
    string trainName;
    vector<Passenger> passengers;

public:
    Train(int tno, string tname) {
        trainNumber = tno;
        trainName = tname;
    }

    void bookTicket(string name, int age, string src, string dest) {
        Passenger p(name, age, src, dest);
        passengers.push_back(p);
        cout << "✅ Ticket booked successfully!\n\n";
    }

    void displayTrainInfo() {
        cout << "Train No   : " << trainNumber << endl;
        cout << "Train Name : " << trainName << endl;
    }

    void showAllPassengers() {
        if (passengers.empty()) {
            cout << "🚫 No passengers booked yet.\n";
            return;
        }

        cout << "\n📋 Passenger List:\n";
        for (Passenger &p : passengers) {
            p.displayPassenger();
        }
    }
};

int main() {
    Train t1(12345, "Rajdhani Express");
    Train t2(12346, "Shatabdi Express");
    Train t3(12347, "Amrapali Express");

    int choice;
    do {
        cout << "\n===== RAILWAY BOOKING SYSTEM =====" << endl;
        cout << "1. Book Ticket" << endl;
        cout << "2. Show All Passengers" << endl;
        cout << "3. Train Info" << endl;
        cout << "0. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1: {
            string name, source, destination;
            int age;
            cout << "Enter Name: ";
            cin.ignore();
            getline(cin, name);
            cout << "Enter Age: ";
            cin >> age;
            cout << "Enter Source: ";
            cin >> source;
            cout << "Enter Destination: ";
            cin >> destination;
            t1.bookTicket(name, age, source, destination);
            break;
        }
        case 2:
            t1.showAllPassengers();
            break;
        case 3:
            t1.displayTrainInfo();
            break;
        case 0:
            cout << "👋 Exiting Railway Booking System. Have a safe journey!" << endl;
            break;
        default:
            cout << "❌ Invalid choice. Try again!" << endl;
        }
    } while (choice != 0);

    return 0;
}
 