#include<iostream>
using namespace std;
int main(){
    int num1[99],sum=0,avg;
    int i,j,no;
    cout<<"Enter the size of the Array:";
    cin>>no;
    cout<<"Enter the elements of the first array:"<<endl;
    for(i=0;i<no;i++){
            cout<<"Enter a Number: ";
            cin>>num1[i];
    }
    cout<<"============Sum of Array============"<<endl;
    for(i=0;i<no;i++){
        sum+=num1[i];
    }
    cout<<"Sum of Array is "<<sum<<endl;
    cout<<"============Average of Array============"<<endl;
    avg=sum/no;
    cout<<"Average of Array is "<<avg;
     return 0;
}