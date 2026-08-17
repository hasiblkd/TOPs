import math as m

bill_amt=float(input("Enter a Bill Amount:-"))
discount=float(input("Enter a Discount Amount:-"))

discount_amt=(bill_amt*discount)/100

final_bill=bill_amt-discount_amt

ans=m.floor(final_bill)

print("Final Bill:-",ans)