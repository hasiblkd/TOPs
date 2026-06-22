#include<iostream>
using namespace std;
int main() {
    int a = 10, b = 5;
    cout << "Arithmetic Operators:" << endl;
    cout << "Addition: " << a + b << endl;
    cout << "Subtraction: " << a - b << endl;
    cout << "Multiplication: " << a * b << endl;
    cout << "Division: " << a / b << endl;
    cout << "Modulus: " << a % b << endl;

    cout << "\nRelational Operators:" << endl;
    cout << "a > b : " << (a > b) << endl;
    cout << "a < b : " << (a < b) << endl;
    cout << "a == b : " << (a == b) << endl;
    cout << "a != b : " << (a != b) << endl;

    cout << "\nLogical Operators:" << endl;
    cout << "(a > 0 && b > 0) : " << (a > 0 && b > 0) << endl;
    cout << "(a > 0 || b < 0) : " << (a > 0 || b < 0) << endl;
    cout << "!(a > b) : " << !(a > b) << endl;

    cout << "\nBitwise Operators:" << endl;
    cout << "a & b : " << (a & b) << endl;
    cout << "a | b : " << (a | b) << endl;
    cout << "a ^ b : " << (a ^ b) << endl;
    cout << "a << 1 : " << (a << 1) << endl;
    cout << "a >> 1 : " << (a >> 1) << endl;

    return 0;
}