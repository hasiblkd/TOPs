import re as re

# st="Sun rise in the East"

# k=re.match("in",st)
# k=re.search("in",st)
# k=re.findall("in",st)
# k=re.finditer("in",st)
# print(next(k))
# print(next(k))

# k=re.sub("in","k",st)
# k=re.split(" ",st)
# print(k)

st=" a quick foxx brown foox jump fx over lazy dog 323 rer 55"

# k=re.findall("f.x",st)
# k=re.search("^fox",st)
# k=re.search("fox$",st)
# k=re.findall("fo*x",st)
# k=re.findall("fo+x",st)
# k=re.findall("fo?x",st)

# k=re.findall("\d",st)
# k=re.findall("\D",st)
# k=re.findall("\w",st)
# k=re.findall("\W",st)
# k=re.findall("\s",st)
# k=re.findall("\S",st)
# k=re.findall(r"\bcat\b","cat in catelog")
# k=re.findall(r"\Bcat\B","cat in abccatelog")
# print(k)

# phone=8347906205
# k=re.match(r"^\d{10$",phone)
# if k is None:
#     print("Invalid")
# else:
#     print("Valid")

# email="hasiblkd123@gmail.com"
# k=re.match(r"^[a-z0-9]+@[a-z]+\.[a-z]{2,4}$",email)
# print(k)

user_name="Hasib"
k=re.match(r"\D{3,10}",user_name)
print(k)