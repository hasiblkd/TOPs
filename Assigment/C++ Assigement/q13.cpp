#include<iostream>
using namespace std;
int FunFact(int n){
    if(n==0||n==1){
        return 1;
    }
    else{
        return n*FunFact(n-1);
    }
}
int main(){
    int num;
    cout<<"Enter a number: ";
    cin>>num;
    cout<<"Factorial of "<<num<<" is "<<FunFact(num)<<endl;
     return 0;
}