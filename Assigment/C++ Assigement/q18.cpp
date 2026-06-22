#include<iostream>
using namespace std;
class Calculator{
    public:
    int add(int a,int b){
        return a+b;
    }
    int subtract(int a,int b){
        return a-b;
    }
    int multiply(int a,int b){
        return a*b;
    }
    float divide(int a,int b){
        if(b==0){
            cout<<"Error: Division by zero!"<<endl;
            return 0;
        }
        return (float)a/b;
    }
};
int main(){
    Calculator calc;
    int num1,num2;
    cout<<"Enter  number 1: ";
    cin>>num1;
    cout<<"Enter  number 2: ";
    cin>>num2;
    cout<<"Addition: "<<calc.add(num1,num2)<<endl;
    cout<<"Subtraction: "<<calc.subtract(num1,num2)<<endl;
    cout<<"Multiplication: "<<calc.multiply(num1,num2)<<endl;
    cout<<"Division: "<<calc.divide(num1,num2)<<endl;
    return 0;
}