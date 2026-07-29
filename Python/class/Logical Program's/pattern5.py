num=int(input("Enter a No. of Row:-"))
for i in range(num-1):
    for j in range(num-i):
        print("",end="")
    for k in range(i+1):
        print("* ",end="")
    print()

for i in range(num):
    for j in range(i+1):
        print("",end="")
    for k in range(num-i):
        print("* ",end="")
    print()