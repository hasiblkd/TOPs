import re


def is_valid_pnr(pnr):
    pattern=r"^\d{10}$"
    result=re.match(pattern, pnr)

    if result:
        return True
    else:
        return False


pnr=input("Enter PNR Number: ")

if is_valid_pnr(pnr):
    print("Valid PNR")
else:
    print("Invalid PNR")