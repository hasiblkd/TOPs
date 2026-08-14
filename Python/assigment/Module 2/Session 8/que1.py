def product(price,quntity):
    final_price=price*quntity
    print("Final Total is:-",final_price)

p_price=float(input("Enter price of Product:-"))
p_quntity=int(input("Enter Quntity of Product:-"))

product(p_price,p_quntity)