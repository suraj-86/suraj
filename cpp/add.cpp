//function overloading

#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}
float add(float a, float b) {
    return a + b;
}
double add(double a, double b) {
    return a + b;
}
int add(int a, int b, int c) {
    return a + b + c;
}
int main() {
    int a = 10,b = 20,g=30;
    float c = 10.5 ,d = 20.7;
    double e = 10.123, f = 20.456;
    cout << add(a, b) << endl;
    cout << add(c, d) << endl;
    cout << add(e, f) << endl;
    cout << add(a,b,g) << endl;
}