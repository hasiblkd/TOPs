#include<iostream>
using namespace std;
int Addition(int a, int b){
    return a+b;
};
int Subtraction(int a, int b){
    return a-b;
}
int Multiplication(int a, int b){
    return a*b;
}
float Division(int a, int b){
    if(b!=0){
        return (float)a/b;
    }
    else{
        cout<<"Error: Division by zero is not allowed."<<endl;
    }
}
int main(){
    int a,b;
    int add,sub,mul,div;
    cout<<"Enter Number 1:";
    cin>>a;
    cout<<"Enter Number 2:";
    cin>>b;
    add=Addition(a,b);
    sub=Subtraction(a,b);
    mul=Multiplication(a,b);
    div=Division(a,b);
    cout<<"Addition: "<<add<<endl;
    cout<<"Subtraction: "<<sub<<endl;
    cout<<"Multiplication: "<<mul<<endl;    
    cout<<"Division: "<<div<<endl;
     return 0;

}