with open("order.txt","w") as f:
    f.write("Pizza\n")
    f.write("Burger\n")
    f.write("Sandwich\n")
    f.write("Momos\n")
    f.write("Shawarma")
    f.close()

with open("order.txt","r") as f:
    while True:
        order=f.readline()
        if order=="":
            break
        print("Order:", order.strip())
        print("Pointer Position:", f.tell())
    f.close()