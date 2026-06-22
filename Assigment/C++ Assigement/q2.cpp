#include<iostream>
using namespace std;
int main(){
    int age;
    char name[50];
    cout<<"Enter your name: ";
    cin.getline(name, 50);
    cout<<"Enter your age: ";
    cin>>age;
    cout<<"Name: "<<name<<endl;
    cout<<"Age: "<<age<<endl;
    return 0;
}