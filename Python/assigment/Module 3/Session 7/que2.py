class Payment:
    def Pay(self,amt):
        self.amt=amt
        print("Paying",self.amt)
        

class UPI:
    def Pay(self,amt):
        self.amt=amt
        print("Paying",self.amt)

amt=float(input("Enter Paying Amount:-"))

p1=Payment()
u1=UPI()

p1.Pay(amt)
u1.Pay(amt)
