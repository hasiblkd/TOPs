class PaymentFieldError(Exception):
    def __init__(self,msg):
                super().__init__(msg)

def procces_payment(amount):
        if amount<0:
            raise PaymentFieldError("Payment Must Greater then 0.....")
        else:
            print("Payment Succsecfull.....")

try:
    amt=int(input("Enter Amount:-"))
    procces_payment(amt)

except PaymentFieldError as e:
    print(e)
