#include<iostream>
using namespace std;
int num = 100;
void display() {
    int num = 50;
    cout << "Local Variable inside function: " << num << endl;
    cout << "Global Variable inside function: " << ::num << endl;
}
int main() {
    cout << "Global Variable inside main: " << num << endl;
    display();
    return 0;
}