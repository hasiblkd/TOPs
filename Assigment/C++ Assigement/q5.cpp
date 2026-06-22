#include<iostream>
using namespace std;
int main(){
    int a;
    float b;
    char c[50];

    const float pi = 3.14;

    cout<<"Enter an integer: ";
    cin>>a;
    cout<<"Enter a float: ";
    cin>>b;
    cout<<"Enter a string: ";
    cin>>c;
    cout<<"You entered integer: "<<a<<endl;
    cout<<"You entered float: "<<b<<endl;
    cout<<"You entered string: "<<c<<endl;

    a+=10;
    b+=4.5;
    cout<<"After adding 10 to integer: "<<a<<endl;
    cout<<"After adding 4.5 to float: "<<b<<endl;

    float radius;
    cout<<"Enter the radius of a circle: ";
    cin>>radius;
    float area = pi * radius * radius;
    cout<<"Area of the circle: "<<area<<endl;
    return 0;
    
}