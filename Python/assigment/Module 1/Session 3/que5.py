num1=int(input("Enter a Number 1:-"))
num2=int(input("Enter a Number 2:-"))
ch=input(("""
    1. +(Addition)
    2. -(Subtraction)
    3. *(Multiplication)
    4. /(Division)

    Enter Your Choice:-
"""))

match(ch):
    case '+':
        print("Addition is ",num1+num2)
    case '-':
        print("Subtraction is ",num1-num2)
    case '*':
        print("Multiplication is ",num1*num2)
    case '/':
        print("Division is ",num1/num2)
    case _:
        print("Invalid Choice........")