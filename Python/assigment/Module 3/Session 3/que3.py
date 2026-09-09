try:
    wallet_balance=1000
    ticket=int(input("Enter a Number of Ticket:-"))
    print("Your Wallet Balance:-",wallet_balance)
    price_per_Ticker=wallet_balance/ticket
    print("Price of Per Ticket is",price_per_Ticker)
except ZeroDivisionError:
    print("0 is Not Allowed")
except ValueError:
    print("Enter a Valied Number's.....")