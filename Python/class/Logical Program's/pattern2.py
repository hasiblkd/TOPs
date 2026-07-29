num=int(input("Enter a Number:-"))
for i in range(num):
    for j in range(i+1):
        print(" ",end="")
    for k in range(num-i):
        print("* ",end="")
    print()