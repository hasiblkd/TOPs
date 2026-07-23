balance=float(input("Enter Your Balance:-"))
panlty=100
if balance<=1000:
    print("Your current balance is ",balance,"So, You might have to Face Panalty of no Maintain balace of more then 1000...")
    balance-=panlty
    print(" After a Panelty...","Your Current Balance is ",balance,".")
    print("PLZ Maintaine Your Balance to Avoid Panelty...")
else:
    if balance>=1001:
        print("Your Current Balance is ",balance,".")
        print("Thanks For Maintain Balance...")