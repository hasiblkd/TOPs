#include<iostream>
using namespace std;
int main(){
    char name[100], grade[20];
    int marks;

    cout<<"Enter your name: ";
    cin.getline(name, 100);
    cout<<"Enter your marks: ";
    cin>>marks;
    cout<<"Name: "<<name<<endl;
    cout<<"Marks: "<<marks<<endl;
    if(marks>=90){
        cout<<"Grade: A"<<endl;
    }
    else if(marks>=80){
        cout<<"Grade: B"<<endl;
    }
    else if(marks>=70){
        cout<<"Grade: C"<<endl;
    }
    else if(marks>=60){
        cout<<"Grade: D"<<endl;
    }
    else{
        cout<<"Grade: F"<<endl;
    }
     return 0;
}