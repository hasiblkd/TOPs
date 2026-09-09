import re

gmail=input("Enter a Gmail id:-")

valid=re.match(r"^[a-z0-9]+@[a-z]+\.[a-z]{2-4}$",gmail)
if valid:
    print("Valied")
else:
    print("Not Valied")


