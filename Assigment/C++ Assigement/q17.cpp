#include<iostream>
#include<string>
using namespace std;
int main(){
    string str,rev="";
    int i;
    cout<<"Enter a String: ";
    cin>>str;
    for(i=str.length()-1;i>=0;i--){
        rev+=str[i];
    }
    cout<<"Reverse of String is: "<<rev<<endl;
    if(str==rev){
        cout<<"String is Palindrome"<<endl;
    }
    else{
        cout<<"String is not Palindrome"<<endl;
    }
}