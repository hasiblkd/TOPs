age=int(input("Enter a Your Age:-"))
time=int(input("Enter a current time in 24-Hour Formet:-"))

if age>18:
    if time>=20 and time<=24:
        print("Your Are Allowed for Ordering Food...")
    else:
        print("Your Are Allowed for Ordering Food Becuse your Are Out of time...")
else:
    print("Your not Allowed For Ordering Food becuse of your Age...")