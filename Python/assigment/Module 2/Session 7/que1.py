ch=input("Enter a any word:-")
count={}
for i in ch:
    if i in count:
        ch[i]+=1
    else:
        ch[i]=1
print(count)