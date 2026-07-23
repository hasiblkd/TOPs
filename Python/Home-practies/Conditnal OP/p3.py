age=int(input("Enter your Age:-"))
if age<=5:
    print("Your Movie Ticket is Free....")
else:
    if age>=6 and age<=12:
        print("Your Movie Ticket price is ₹100.")
    elif age>=13 and age<=60:
        print("Your Movie Ticket price is ₹200.")
    else:
        print("Your Movie Ticket price is ₹120.")