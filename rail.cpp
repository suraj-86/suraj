#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class Train {
    private:
        int trainNo;
        string trainName;
        string source, destination;
        string time;
    public:
        void setDetails(int no, string name, string src, string dest, string t);
        void showDetails();
        int getTrainNo() const { return trainNo; }  // To access train number
};

void Train::setDetails(int no, string name, string src, string dest, string t) {
    trainNo = no;
    trainName = name;
    source = src;
    destination = dest;
    time = t;
}

void Train::showDetails() {
    cout << "Train No: " << trainNo << endl;
    cout << "Train Name: " << trainName << endl;
    cout << "Source: " << source << endl;
    cout << "Destination: " << destination << endl;
    cout << "Time: " << time << endl;
}

class Booking {
    private:
        string passengerName;
        int age;
        int trainNo;
    public:
        void bookTicket();
        void viewTicket();
};

void Booking::bookTicket() {
    ofstream file("bookings.txt", ios::app);
    if (!file) {
        cout << "Error opening file!\n";
        return;
    }

    cout << "Enter passenger name: ";
    cin.ignore();  // To clear the buffer for getline
    getline(cin, passengerName);  // Allows for full names with spaces

    cout << "Enter age: ";
    cin >> age;
    cout << "Enter train number: ";
    cin >> trainNo;

    file << passengerName << " " << age << " " << trainNo << endl;
    file.close();
    cout << "Ticket booked successfully!\n";
}

void Booking::viewTicket() {
    ifstream file("bookings.txt");
    if (!file) {
        cout << "Error opening file!\n";
        return;
    }

    string name;
    int age, trainNo;
    cout << "\nBooked Tickets:\n";
    while (file >> name >> age >> trainNo) {
        cout << "Passenger: " << name << ", Age: " << age << ", Train No: " << trainNo << endl;
    }
    file.close();
}

int main() {
    const int MAX_TRAINS = 10;  // Maximum number of trains
    Train trains[MAX_TRAINS];   // Array to store multiple trains
    int trainCount = 0;         // To keep track of the number of trains added

    Booking b;

    int choice;
    do {
        cout << "\nMenu:\n";
        cout << "1. View Train Details\n";
        cout << "2. Book Ticket\n";
        cout << "3. View Tickets\n";
        cout << "4. Add a Train\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                // Show train details
                if (trainCount == 0) {
                    cout << "No trains available.\n";
                } else {
                    cout << "Available Trains:\n";
                    for (int i = 0; i < trainCount; i++) {
                        cout << "Train " << (i + 1) << ":\n";
                        trains[i].showDetails();
                        cout << endl;
                    }
                }
                break;
            case 2:
                // Book a ticket
                b.bookTicket();
                break;
            case 3:
                // View booked tickets
                b.viewTicket();
                break;
            case 4:
                // Add a new train
                if (trainCount < MAX_TRAINS) {
                    int trainNo;
                    string name, source, destination, time;

                    cout << "Enter train number: ";
                    cin >> trainNo;
                    cin.ignore(); // to clear the buffer before reading strings
                    cout << "Enter train name: ";
                    getline(cin, name);
                    cout << "Enter source: ";
                    getline(cin, source);
                    cout << "Enter destination: ";
                    getline(cin, destination);
                    cout << "Enter time: ";
                    getline(cin, time);

                    trains[trainCount].setDetails(trainNo, name, source, destination, time);
                    trainCount++;  // Increment the count after adding a new train
                    cout << "Train added successfully!\n";
                } else {
                    cout << "Cannot add more trains. Maximum limit reached.\n";
                }
                break;
            case 5:
                cout << "Exiting program...\n";
                break;
            default:
                cout << "Invalid choice! Please enter a valid option.\n";
        }
    } while (choice != 5);

    return 0;
}
