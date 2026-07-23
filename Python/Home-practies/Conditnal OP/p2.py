current_pin=1234
balance=50000
ask_pin=int(input("Enter a pin:-"))
if current_pin==ask_pin:
    print("ATM PIN is Correct...")
    withdraw_amt=float(input("Enter a amount:"))
    if balance>=withdraw_amt:
        balance-=withdraw_amt
        print("Witdrew Succesfully...")
        print("After Withdraw Money, Your Current Balance is ",balance)
    else:
        print("You enter this ",withdraw_amt,". ","But Your Current Balance is ",balance,".")
        print("Influence Balance...")
else:
    print("Wrong ATM PIN...")