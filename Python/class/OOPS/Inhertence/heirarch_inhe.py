class Account:

    balance=0
    def get_balnce(self):
        print("Current Amount:-",self.balance)

    def deposit(self,amount):
        pass

    def withdraw(self,amount):
        pass

class Saving(Account):
    def deposit(self, amount):
        self.balance=amount

    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficint Balance......")
        else:
            self.balance-=amount

class Loan(Account):
    def withdraw(self, amount):
        self.balance+=amount

    def deposit(self, amount):
        if amount>self.balance:
            k=amount-self.balance
            print("Your Loan is Cleared   -   Your Return Amount is ",k)
            self.balance=0
        else:
            self.balance-=amount

s= Saving()
s.get_balnce()
s.deposit(5000)
s.get_balnce()
s.deposit(3000)
s.get_balnce()
s.withdraw(1000)
s.get_balnce()

# l=Loan()
# l.get_balnce()
# l.withdraw(5000)
# l.get_balnce()
# l.deposit(1000)
# l.get_balnce()