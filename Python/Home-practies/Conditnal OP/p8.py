print("Select Your Choice")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
ch=input("Enter your choice")
a=int(input("Enter a number:-"))
b=int(input("Enter a number:-"))

match ch:
    case "1":
        c=a+b
        print("Addition is ",c)
    case "2":
        c=a-b
        print("Subtraction is ",c)
    case "3":
        c=a*b
        print("Multiplication is ",c)
    case "4":
        c=a/b
        print("Division is ",c)
    case _:
        print("Invalid Choice...")