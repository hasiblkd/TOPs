import re

text=input("Enter text with Mobile Number:-")

valied=re.search(r"\b\d{10}\b",text)

if valied:
    print("Mobile No:-",valied.group())
else:
    print("Mobile Number not Found.....")