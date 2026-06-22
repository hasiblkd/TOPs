#include<stdio.h>
#include<iostream>
using namespace std;
double RectangleArea(){
    double area, length, width;
    cout<<"POP to Calculate the area of a rectangle"<<endl;
    cout<<"Enter the length of the rectangle: ";
    cin>>length;
    cout<<"Enter the width of the rectangle: ";
    cin>>width;
    area = length * width;
    cout<<"The area of the rectangle is: "<<area<<endl;
    return area;
};
class areaRectangle{
    public:
        double area, length, width;
        void getdata(){
            cout<<"OOP to Calculate the area of a rectangle"<<endl;
            cout<<"Enter the length of the rectangle: ";
            cin>>length;
            cout<<"Enter the width of the rectangle: ";
            cin>>width;
        }
        void display(){
            area = length * width;
            cout<<"The area of the rectangle is: "<<area<<endl;
        }
};
int main(){
    RectangleArea();
    areaRectangle r;
    r.getdata();
    r.display();
    return 0;
}