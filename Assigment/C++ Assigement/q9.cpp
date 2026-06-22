#include<iostream>
using namespace std;
int main(){
    int number=45,guess;
    cout<<"Guess the number between 1 and 100: "<<endl;
    while(guess!=number){
        cout<<"Enter your guess: ";
        cin>>guess;
        if(guess>number){
            cout<<"Too high! Try again."<<endl;
        }
        else if(guess<number){
            cout<<"Too low! Try again."<<endl;
        }
        else{
            cout<<"Congratulations! You guessed the number."<<endl;
        }
        
    }
    
}