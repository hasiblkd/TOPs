print("Resturent Menu")
print("1.Pizza ₹250")
print("2.Burger ₹150")
print("3.Sandwich ₹120")
print("4.coffe ₹80")

ch=int(input("Enter your choice::"))
#item=int(input("Enter a item::"))
quantity=int(input("Enter Quantity::"))
bill=0
discount=0
final_total=0

if quantity<0:
    print("Invalid Quantity...")

match ch:
    case 1:
        print("You order a Pizza...")
        print("Your Quantity is ",quantity)
        bill=250*quantity
        print("Your bill is ",bill)
        if bill>1000:
            discount=bill*0.10
            print("Your Order More then ₹1000. So you get 10% Discount...")
            print("Your Discount Amount is ",discount,".")
            final_total=bill-discount
            print("Total Amount of Bill is ",final_total,".")
    case 2:
        print("You order a Burger...")
        print("Your Quantity is ",quantity)
        bill=150*quantity
        print("Your bill is ",bill)
        if bill>=1000:
            discount=bill*0.10
            print("Your Order More then ₹1000. So you get 10% Discount...")
            print("Your Discount Amount is ",discount,".")
            final_total=bill-discount
            print("Total Amount of Bill is ",final_total,".")
    case 3:
        print("You order a Sandwich...")
        print("Your Quantity is ",quantity)
        bill=120*quantity
        print("Your bill is ",bill)
        if bill>1000:
            discount=bill*0.10
            print("Your Order More then ₹1000. So you get 10% Discount...")
            print("Your Discount Amount is ",discount,".")
            final_total=bill-discount
            print("Total Amount of Bill is ",final_total,".")
    case 4:
        print("You order a Coffe...")
        print("Your Quantity is ",quantity)
        bill=80*quantity
        print("Your bill is ",bill)
        if bill>1000:
            discount=bill*0.10
            print("Your Order More then ₹1000. So you get 10% Discount...")
            print("Your Discount Amount is ",discount,".")
            final_total=bill-discount
            print("Total Amount of Bill is ",final_total,".")
    case _:
        print("Invalid Choice")