num=int(input("Enter a No. of Row:-"))
for i in range(num-1):
    for j in range(num-i):
        print(" ",end="")
    for k in range(i+1):
        if k==0 or k==i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

for i in range(num):
    for j in range(i+1):
        print(" ",end="")
    for k in range(num-i):
        if k==0 or k==num-(i+1):
            print("* ",end="")
        else:
            print("  ",end="")
    print()