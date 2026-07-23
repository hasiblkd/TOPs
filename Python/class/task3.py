print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Press any to exit")
num1=int(input("Enter a number::"))
num2=int(input("Enter a number::"))
ch=int(input("Enter your Choice::"))

match(ch):
    case 1:
        add=num1+num2
        print("Addition is ",add)
    case 2:
        sub=num1-num2
        print("Subtraction is ",sub)
    case 3:
        mul=num1*num2
        print("Multiplication is ",mul)
    case 4:
        div=num1/num2
        print("Division is ",div)
    case _:
        print("Invalied choice")