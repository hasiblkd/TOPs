try:
    price=int(input("Enter a price of Product:-"))
    quntity=int(input("Enter a Quntity of Product:-"))
    bill=price*quntity
    print("Total Bill:-",bill)
except ValueError:
    print("Enter a Valied Input......")