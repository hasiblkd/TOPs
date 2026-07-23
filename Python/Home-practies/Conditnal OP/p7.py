amount=float(input("Enter Your Shopping Amount:-"))
disc_amt=0
final_amt=0
if amount<0:
    print("Invalid Input")
elif amount<999:
        print("Your Shopping Amount is ",amount,".")
        print("You get No Discount...")
elif amount>=1000 and amount<=4999:
        print("Your Shopping Amount is ",amount,".")
        print("You get 10% Discount...")
        disc_amt=amount*0.10
        print("Your Discount Amount is ",disc_amt)
        final_amt=amount-disc_amt
        print("Your Final Total is ",final_amt)

elif amount>=5000 and amount<=9999:
        print("Your Shopping Amount is ",amount,".")
        print("You get 20% Discount...")
        disc_amt=amount*0.20
        print("Your Discount Amount is ",disc_amt)
        final_amt=amount-disc_amt
        print("Your Final Total is ",final_amt)
        
else:
        print("Your Shopping Amount is ",amount,".")
        print("You get 30% Discount...")
        disc_amt=amount*0.30
        print("Your Discount Amount is ",disc_amt)
        final_amt=amount-disc_amt
        print("Your Final Total is ",final_amt)