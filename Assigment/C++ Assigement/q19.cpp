#include<iostream>
using namespace std;
class BankAccount{
    private:
        float balance;
    public:
        void setBalance(){
            cout<<"Enter  balance: ";
            cin>>balance;
        }
        void DepositBalance(){
            float amount;
            cout<<"Enter  amount to deposit: ";
            cin>>amount;
            balance+=amount;
            cout<<"New balance after deposit: "<<balance<<endl;
        }
        void WithdrawBalance(){
            float amount;
            cout<<"Enter  amount to withdraw: ";
            cin>>amount;
            if(amount>balance){
                cout<<"Error: Insufficient balance!"<<endl;
            }else{
                balance-=amount;
                cout<<"New balance after withdrawal: "<<balance<<endl;
            }
        }
        void DisplayBalance(){
            cout<<"Current balance: "<<balance<<endl;
        }
};
int main(){
    BankAccount account;
    account.setBalance();
    account.DepositBalance();
    account.WithdrawBalance();
    account.DisplayBalance();
    return 0;
}