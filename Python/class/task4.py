import string

text =input("""Enter Food Delivery App Review:-""")

words = [word.lower().strip(string.punctuation) 
         for word in text.split()]

count = {}

for word in words:
    count[word] = words.count(word)

print(count)