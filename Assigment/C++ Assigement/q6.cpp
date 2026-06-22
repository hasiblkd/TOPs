#include<iostream>
using namespace std;
int main() {
    int num1 = 10;
    float num2;
    num2 = num1;
    cout << "Implicit Type Conversion:" << endl;
    cout << "Integer value: " << num1 << endl;
    cout << "Converted Float value: " << num2 << endl;
    float marks = 89.75;
    int finalMarks;
    finalMarks = (int)marks;
    cout << "\nExplicit Type Conversion:" << endl;
    cout << "Original Float value: " << marks << endl;
    cout << "Converted Integer value: " << finalMarks << endl;
    return 0;
}