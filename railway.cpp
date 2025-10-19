#include<iostream>
#include<fstream>
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
        cout << "Enter passenger name: ";
        cin >> passengerName;
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
        string name;
        int age, trainNo;
        cout << "\nBooked Tickets:\n";
        while (file >> name >> age >> trainNo) {
            cout << "Passenger: " << name << ", Age: " << age << ", Train No: " << trainNo << endl;
        }
        file.close();
    }

    int main() {
        Train t;
        t.setDetails(1234, "Shatabdi Express", "Lucknow", "Delhi", "10:00 AM");    
        Booking b;
        int choice;
        do {
            cout << "\nMenu:\n";
            cout << "1. View Train Details\n";
            cout << "2. Book Ticket\n";
            cout << "3. View Tickets\n";
            cout << "4. Exit\n";
            cout << "Enter your choice: ";
            cin >> choice;
    
            switch (choice) {
                case 1:
                    t.showDetails();
                    break;
                case 2:
                    b.bookTicket();
                    break;
                case 3:
                    b.viewTicket();
                    break;
                case 4:
                    cout << "Exiting program...\n";
                    break;
                default:
                    cout << "Invalid choice! Please enter a valid option.\n";
            }
        } while (choice != 4);
    
        return 0;
    }