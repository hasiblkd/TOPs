print("======BANKING SYSTEM=====")
print("1. Deposit Money")
print("2. Withdrew Money")
print("3. Check Balance")
print("=========================")

flag='y'

current_balance=0
deposite_money=0
withdrew_money=0

while flag=='y':
    ch=input("Enter your choice:")

    match(ch):
        case "1":
            if deposite_money<0:
                print("Invalid Balance")
            else:
                deposite_money=float(input("Enter your Deposite money::"))
                current_balance+=deposite_money
        
        case "2":
            withdrew_money=float(input("Enter Withdrew Money:"))
            if withdrew_money<0:
                print("Invalid Balance")
            elif current_balance<=withdrew_money:
                print("Low Balance...")
                print("You want ",withdrew_money,"but Your Current Balance is ",current_balance)
            else:
                current_balance-=withdrew_money
                print("Withdraw Succesful..")
        case "3":
            print("Your Current Balance is ",current_balance)
        case _:
            print("Invalied Choice...")
        
    flag=input("if you want to continue then press 'y' and not so press 'n':")
    if flag=='n':
        print("Your are Exit...")