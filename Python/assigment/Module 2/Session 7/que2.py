review=input("Enter any Food delivery App Review:-")
word=""

for i in review:
    if i.isalnum():
        word+=i

print(word.lower())