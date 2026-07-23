unit=int(input("Enter a unit:-"))
price=0
if unit<0:
    print("invalid Unit...")
else:
    if unit>=0 and unit<=100:
        print("per Unit ₹2...")
        price=unit*2
        print("Your Billing Amount is ",price)
    elif unit>=101 and unit<=300:
        print("per Unit ₹5...")
        price=unit*5
        print("Your Billing Amount is ",price)
    elif unit>=300:
        print("per Unit ₹8...")
        price=unit*8
        print("Your Billing Amount is ",price)