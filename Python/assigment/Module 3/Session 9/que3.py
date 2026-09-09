import re

def extract_hastag(text):
    hastag=re.findall(r"#\w+",text)
    return hastag

caption=input("Enter Instagram Caption:-")
result=extract_hastag(caption)
print("Hastag:-",result)