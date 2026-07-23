side1=int(input("Enter a Side 1:"))
side2=int(input("Enter a Side 2:"))
side3=int(input("Enter a Side 3:"))
if side1==side2 and side1==side3 and side2==side1 and side2==side3 and side3==side1 and side3==side2:
    print("All Side Are match...")
    print("It's Triangle...")
else:
    print("All Side Are not match...")
    print("It's not a Triangle...")