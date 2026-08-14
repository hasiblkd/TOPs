def apply_coupon(amount,cupon_code="none"):
    if cupon_code=="SAVE10%":
        discount=(amount*10)/100
        final_price=amount-discount
        print("Amount:-",amount)
        print("Coupon Code:-",cupon_code)
        print("Final Price:-",final_price)
    else:
        print("Amount:-",amount)
        print("Coupon Code:-",cupon_code)

apply_coupon(amount=1000,cupon_code="SAVE10%")